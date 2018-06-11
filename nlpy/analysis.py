import sys 
sys.path.append("../")

from konlpy.tag import Kkma
from konlpy.utils import pprint


class Analaysis:
	def __init__(self):
		self.kkma = Kkma()	
		self.senti_result = "-"
		self.makeDic()

	def getNounsList(self,sentence,length=0):			
		self.nousList = list(filter(lambda x: len(x) > length, self.kkma.nouns(sentence)))		
		return self.nousList

	def makeDic(self):
		self.positive_arr = self.readTxt("./res/dictionary/positive-words-ko-v2.txt")
		self.negative_arr = self.readTxt("./res/dictionary/negative-words-ko-v2.txt")

	def readTxt(self,dir):
		arr = []	
		f = open(dir, 'r')
		while True:
		    line = f.readline()
		    if not line: break
		    arr.append(line.strip())
		f.close()
		return arr

	def checkSentiment(self,nlpy_sententse):
		posScore = 0;
		negScore = 0;
		sumScore = 0;

		for nous in nlpy_sententse:
			for pos in self.positive_arr:
				# 긍정 사전안에 포함되었다면
				if pos in nous:
					print("p-> "+pos)
					posScore =  posScore + 1;
			for neg in self.negative_arr:
				# 부정 사전안에 포함되었다면
				if neg in nous:
					print("n-> "+neg)
					negScore =  negScore + 1;									

		# print("posScore = " + str(posScore))
		# print("negScore = " + str(negScore))
		# print("sumScore = " + str(sumScore))		
		sumScore = posScore + negScore 	

		if sumScore==0:
			return "-"
		elif sumScore>0:
			return "P"
		else :
			return "N"


# a = Analaysis()
# a.getNounsList("통일은 감동적이다.")
# a.makeDic()
# print(a.checkSentiment())
