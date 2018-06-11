

# 트위터 검색: https://twitter.com/search?q=통일&src=typd&lang=ko 
# 상세 주소: https://twitter.com/won0207/status/992484290091859968


import sys
sys.path.insert(0,'..')
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from common import util
from manager import DBManager
from model import tweetModel
import os
import json

parent_dir = os.path.abspath('..')
crawling_start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
result = []
search_id = ""
def crawler(driver,cursor,end_date):	
	try:

		streams = driver.find_element_by_id('stream-items-id')
		items = streams.find_elements_by_class_name("stream-item")	
		size_diff = len(items)-len(result) 

		if(len(result) > len(items)):
			time.sleep(2)   
			streams = driver.find_element_by_id('stream-items-id')
			items = streams.find_elements_by_class_name("stream-item")	


		for index,item in enumerate(items):
			# print("index: "+s tr(index))
			if(index>=cursor):				
				tmp_json = {}
				data_id = item.get_attribute("data-item-id");
				nick_name = item.find_element_by_class_name('FullNameGroup')
				id_name =  item.find_element_by_class_name('username')
				time_stamp = item.find_element_by_class_name('_timestamp')
				time_stamp = time_stamp.get_attribute("data-time")
				tweet_text = item.find_element_by_class_name('tweet-text')
				reflections = item.find_elements_by_class_name('ProfileTweet-actionCountForPresentation')
				nick_name = nick_name.text
				nick_name = nick_name.replace("\n","")
				
				# print("data-id: "+data_id)
				# print("comment: "+reflections[0].text)
				# print("retweet: "+reflections[1].text)		
				# print("like: "+reflections[3].text)
				print("nick: "+nick_name.strip())
				# print("id: "+id_name.text.strip())
				# print("time: "+time_stamp.strip())
				print("txt: "+tweet_text.text.strip())	


				tmp_json["data_id"] = data_id
				tmp_json["user_nick"] = nick_name.strip()
				tmp_json["user_id"] = id_name.text.strip()
				tmp_json["text"] = tweet_text.text.strip()				
				tmp_json["comment_cnt"] = reflections[0].text if len(reflections[0].text)!=0 else 0									
				tmp_json["retweet_cnt"] = reflections[1].text if len(reflections[1].text)!=0 else 0									
				tmp_json["like_cnt"] = reflections[3].text if len(reflections[3].text)!=0 else 0									
				tmp_json["time"] = float(time_stamp) - (7 * 3600)
				
				end_date_timestamp = time.mktime(datetime.strptime(end_date, "%Y-%m-%d-%H:%M:%S").timetuple()) + (9*3600)
				if(end_date_timestamp>tmp_json["time"]):
					return -99


				user_id = tmp_json["user_id"]
				user_nick = tmp_json["user_nick"]			
				user = tweetModel.getUser(user_id,user_nick)
				published_date = datetime.fromtimestamp(
										int(tmp_json["time"])
									)
				


				if len(user)==0:
					tweetModel.setUser(user_id,user_nick)
					user = tweetModel.getUser(user_id,user_nick)

				tweetModel.setTweet(user[0]["id"],
									tmp_json["data_id"],
									tmp_json["text"],
									tmp_json["comment_cnt"],
									tmp_json["retweet_cnt"],
									tmp_json["like_cnt"],
									datetime.fromtimestamp(
										int(tmp_json["time"])
									).strftime('%Y-%m-%d %H:%M:%S')							
									)	
				tweetModel.setSearchMeta(search_id,tmp_json["data_id"])


				result.append(tmp_json)
			
		return size_diff

	except Exception as e:
		print(str(e))


def runCrawler(search_word,end_date):
	cursor = 0;
	driver = webdriver.Chrome('/Users/yenos/Documents/sangmyung/big/chromedriver_mac64/chromedriver')
	# driver = webdriver.PhantomJS('/Users/yenos/Documents/sangmyung/big/phantomjs-2.1.1-macosx/phantomjs-2.1.1-macosx/bin/phantomjs')	
	driver.get("https://twitter.com/search?q="+search_word+"&src=typd&lang=ko")
	
	while(1) :		
		addedPage = crawler(driver,cursor,end_date)					
		if addedPage == -99:
			break;
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight)");	
		time.sleep(1)   
		cursor += addedPage	

	return addMetaData(search_word)

def addMetaData(search_word):
	final_dic = {}
	final_dic["search_word"] = search_word
	final_dic["end_time"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	final_dic["start_time"] = crawling_start_time
	final_dic["data"] = result	
	final_dic["data_length"] = len(result)
	return final_dic

if __name__=="__main__":
	
	search_name  = sys.argv[1]
	end_date = sys.argv[2]
	tweetModel.setSearch(search_name,end_date,datetime.now().strftime('%Y-%m-%d-%H:%M:%S'))
	
	search_id = tweetModel.getSearch(search_name)[0]["id"]
	
	finalResult = runCrawler(search_name,end_date)

	print("==== result ====");
	print(finalResult)

	with open(parent_dir+'/out/result.json', 'w',encoding='utf-8') as fp:
	    json.dump(finalResult, fp,ensure_ascii=False,indent=4, sort_keys=True)

	
	