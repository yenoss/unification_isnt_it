# 트위터 검색: https://twitter.com/search?q=통일&src=typd&lang=ko 
# 상세 주소: https://twitter.com/won0207/status/992484290091859968

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
result = []

def crawler(driver,cursor):	
	
	# driver = webdriver.PhantomJS()s
	streams = driver.find_element_by_id('stream-items-id')
	items = streams.find_elements_by_class_name("stream-item")	
	for index,item in enumerate(items):
		if(index>=cursor):
			tmp_json = {}
			# print(item.text)
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

			result.append(tmp_json)

	





def runCrawler(search_word,page):
	cursor = 0;
	driver = webdriver.Chrome('/Users/yenos/Documents/sangmyung/big/chromedriver_mac64/chromedriver')
	# driver = webdriver.PhantomJS('/Users/yenos/Documents/sangmyung/big/phantomjs-2.1.1-macosx/phantomjs-2.1.1-macosx/bin/phantomjs')	
	driver.get("https://twitter.com/search?q="+search_word+"&src=typd&lang=ko")
	

	# crawler(0,40);	
	while(cursor<page*20) :		
		print("cursor: "+str(cursor))
		crawler(driver,cursor)	
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight)");	
		time.sleep(2)   
		cursor += 20
		print("result Length: "+str(len(result)))

	return result

if __name__=="__main__":
	# set
	finalResult = runCrawler("통일",3)
	print("==== result ====");
	print(finalResult)
	