

# 트위터 검색: https://twitter.com/search?q=통일&src=typd&lang=ko 
# 상세 주소: https://twitter.com/won0207/status/992484290091859968

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import json


result = []
crawling_start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def crawler(driver,cursor):	
	
	# driver = webdriver.PhantomJS()
	streams = driver.find_element_by_id('stream-items-id')
	items = streams.find_elements_by_class_name("stream-item")	
	for index,item in enumerate(items):
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
			
			print("data-id: "+data_id)
			print("comment: "+reflections[0].text)
			print("retweet: "+reflections[1].text)		
			print("like: "+reflections[3].text)
			print("nick: "+nick_name.strip())
			print("id: "+id_name.text.strip())
			print("time: "+time_stamp.strip())
			print("txt: "+tweet_text.text.strip())	


			tmp_json["data_id"] = data_id
			tmp_json["nick"] = nick_name.strip()
			tmp_json["id"] = id_name.text.strip()
			tmp_json["text"] = tweet_text.text.strip()
			tmp_json["comment_cnt"] = reflections[0].text
			tmp_json["retweet_cnt"] = reflections[1].text
			tmp_json["like_cnt"] = reflections[3].text			
			tmp_json["time"] = float(time_stamp) - (7 * 3600)

			result.append(tmp_json)

def runCrawler(search_word,page):
	cursor = 0;
	driver = webdriver.Chrome('/Users/yenos/Documents/sangmyung/big/chromedriver_mac64/chromedriver')
	# driver = webdriver.PhantomJS('/Users/yenos/Documents/sangmyung/big/phantomjs-2.1.1-macosx/phantomjs-2.1.1-macosx/bin/phantomjs')	
	driver.get("https://twitter.com/search?q="+search_word+"&src=typd&lang=ko")
	
	while(cursor<page*20) :		
		print("cursor: "+str(cursor))
		crawler(driver,cursor)	
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight)");	
		time.sleep(2)   
		cursor += 20		
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
	# set

	finalResult = runCrawler("통일",1)
	print("==== result ====");
	print(finalResult)

	with open('out/result.json', 'w',encoding='utf-8') as fp:
	    json.dump(finalResult, fp,ensure_ascii=False,indent=4, sort_keys=True)

	
	