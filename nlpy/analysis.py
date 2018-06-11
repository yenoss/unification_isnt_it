import sys 
sys.path.append("../")

from konlpy.tag import Kkma
from konlpy.utils import pprint
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

import os
import json
parent_dir = os.path.abspath('')

with open(parent_dir+'/key/conf.json') as conf_json:
	conf = json.load(conf_json)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = conf["googleCredential"]

class Analaysis:
	def __init__(self):
		self.kkma = Kkma()	
		self.client = language.LanguageServiceClient()
		# self.senti_result = "-"
		# self.makeDic()

	def getNounsList(self,sentence,length=0):			
		self.nousList = list(filter(lambda x: len(x) > length, self.kkma.nouns(sentence)))		
		return self.nousList

	# def makeDic(self):
	# 	self.positive_arr = self.readTxt("./res/dictionary/positive-words-ko-v2.txt")
	# 	self.negative_arr = self.readTxt("./res/dictionary/negative-words-ko-v2.txt")

	# def readTxt(self,dir):
	# 	arr = []	
	# 	f = open(dir, 'r')
	# 	while True:
	# 	    line = f.readline()
	# 	    if not line: break
	# 	    arr.append(line.strip())
	# 	f.close()
	# 	return arr

	# 과거 단순 사전으로 검색했을 경우	
	# def checkSentiment(self,nlpy_sententse):
	# 	posScore = 0;
	# 	negScore = 0;
	# 	sumScore = 0;

	# 	for nous in nlpy_sententse:
	# 		for pos in self.positive_arr:
	# 			# 긍정 사전안에 포함되었다면
	# 			if pos in nous:
	# 				print("p-> "+pos)
	# 				posScore =  posScore + 1;
	# 		for neg in self.negative_arr:
	# 			# 부정 사전안에 포함되었다면
	# 			if neg in nous:
	# 				print("n-> "+neg)
	# 				negScore =  negScore + 1;									

	# 	# print("posScore = " + str(posScore))
	# 	# print("negScore = " + str(negScore))
	# 	# print("sumScore = " + str(sumScore))		
	# 	sumScore = posScore + negScore 	

	# 	if sumScore==0:
	# 		return "-"
	# 	elif sumScore>0:
	# 		return "P"
	# 	else :
	# 		return "N"

	def checkSentimentByGoogle(self,text):	
		document = types.Document(
		    content=text,
		    type=enums.Document.Type.PLAIN_TEXT)
		# Detects the sentiment of the text
		sentiment = self.client.analyze_sentiment(document=document).document_sentiment
		# print('Text: {}'.format(text))
		# print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
		_tmp_result = {}
		_tmp_result["score"] = sentiment.score
		_tmp_result["magnitude"] = sentiment.magnitude
		return _tmp_result
		


