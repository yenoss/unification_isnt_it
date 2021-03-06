from common import util
from manager import DBManager


def setUser(user_id,user_nickname):	
	DBManager.query(
					"""
					INSERT INTO uni_user
					(user_id,user_nickname)
					VALUES (%s,%s)					
					"""
					,
					(user_id,user_nickname)
				)	
		
def getUser(user_id,user_nickname):	
	return util.fetch_all_json(
				DBManager.query(
					"""
					SELECT * 
					FROM uni_user 
					WHERE user_id = %s and user_nickname = %s		
					"""
					,
					(user_id,user_nickname)
				))
def setTweet(user_id,data_id,textt,comment_cnt,retweet_cnt,like_cnt,published_time):	
	DBManager.query(
					"""
					INSERT INTO uni_tweets
					(user_id,data_id,textt,comment_cnt,retweet_cnt,like_cnt,published_time)
					VALUES (%s,%s,%s,%s,%s,%s,%s)					
					"""
					,
					(user_id,data_id,textt,comment_cnt,retweet_cnt,like_cnt,published_time)
				)			

def setSearch(search_name,end_date,created_time):
	DBManager.query(
					"""
					INSERT INTO uni_search
					(search_name,end_date,created_time)
					VALUES (%s,%s,%s)					
					"""
					,
					(search_name,end_date,created_time)
				)		

def getSearch(search_name):	
	return util.fetch_all_json(
				DBManager.query(
					"""
					SELECT * 
					FROM uni_search 
					WHERE search_name = %s 
					"""
					,
					(search_name,)
				))	

def setSearchMeta(search_id,tweet_data_id):
	DBManager.query(
					"""
					INSERT INTO uni_search_meta
					(search_id,tweet_data_id)
					VALUES (%s,%s)					
					"""
					,
					(search_id,tweet_data_id)
				)			

def getAllTweets():
	return util.fetch_all_json(
				DBManager.query(
					"""
					SELECT * 
					FROM uni_tweets
					"""
					,
					()
				))	
def getAllValidTweets():
	return util.fetch_all_json(
				DBManager.query(
					"""
					SELECT * FROM  uni_tweets WHERE isValid =1
					"""
					,
					()
				))						
def setTweetSentiment(data_id,sentiment_score,sentiment_magnitude):
	DBManager.query(
					"""
					UPDATE uni_tweets 
					SET sentiment_score = %s,sentiment_magnitude = %s
					where data_id = %s
					"""
					,
					(sentiment_score,sentiment_magnitude,data_id)
				)			


def setTweetValid(data_id):
	DBManager.query(
					"""
					UPDATE uni_tweets 
					SET isValid = 0 
					WHERE data_id = %s
					"""
					,
					(data_id,)
				)			


def getSegmentGood():
	return util.fetch_all_json(
				DBManager.query(
					"""
					SELECT count(*) as good 
					FROM uni_tweets 
					WHERE sentiment_score > 0.25
					"""
					,
					()
				))		
def getSegmentNoraml():	
	return util.fetch_all_json(
				DBManager.query(
					"""
					SELECT count(*) as normal 
					FROM uni_tweets 
					WHERE sentiment_score > -0.25 AND sentiment_score < 0.25
					"""
					,
					()
				))		

def getSegmentBad():	
	return util.fetch_all_json(
				DBManager.query(
					"""
					SELECT count(*) as bad 
					FROM uni_tweets 
					WHERE sentiment_score < -0.25
					"""
					,
					()
				))		