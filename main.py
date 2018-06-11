from nlpy.analysis import Analaysis
from manager import DBManager
from model import tweetModel




def main():    	
	a = Analaysis()	


	tweets = tweetModel.getAllTweets()


	# tokenized_contents = [['평화', '새', '시작', '슬로건', '남북', '남북정상회담', '정상', '회담', '홈페이지', '개설'], ['2018', '남북', '남북정상회담', '정상', '회담', '평화', '새', '시작', '열흘', '앞', '역사적', '순간', '국민', '정상회담', '홈페이지', '온라인', '라이브', '등', '소식', '공개', '예정', '평화회담', '1'], ['임시', '임시국회', '국회', '개정', '개정휴업', '휴업', '중', '정쟁', '시간', '와중', '문', '문재인대통령', '재인', '대통령', '남북', '남북정상회담', '정상', '회담', '준비', '여념', '만일', '우리', '우리나라', '나라', '내각제', '뻔', '생각'], ['속보', '김', '겸', '대변인', '브리핑', '평화', '새', '시작', '남북', '남북정상회담', '정상', '회담', '표어', '11', '11년', '년', '만', '간', '만남', '만남이자', '이자', '북미', '북미정상회담', '길잡이', '세계', '세계평화', '여정', '의미']]
	tokenized_contents = []
	for item in tweets:
		tweet_text = item["textt"]
		# print(tweet_text)
		# print(a.getNounsList(tweet_text))
		tokenized_contents.append(a.getNounsList(tweet_text))
		# print(a.checkSentiment())


	from gensim.models import Word2Vec
	model = Word2Vec(tokenized_contents, min_count=1)
	print(model.most_similar(positive=["통일"], topn=100))



	# embedding_model = Word2Vec(tokenized_contents, size=100, window = 2, min_count=50, workers=4, iter=100, sg=1)
# 

	# print(tokenized_contents)
	# a.getNounsList("통일은 감동적이다.")	
	# print(a.checkSentiment())


if __name__=="__main__":
	main();
