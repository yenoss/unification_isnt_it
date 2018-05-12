## Installation

* Chrome Web Driver
* Selenium 



## TweetCrawler Run & Test

* TweetCrawler Run

```
> python3 crawler/tweetCrawler.py
```

* TweetCrawler test

```
> cd test
> python3 test.py
```





## 주제: 통일 어떻게 생각하세요?

> 통일에 대한 사람들의 생각은 어떨까?

### 1.선정 이유
* 4.27일 남북 정상회담. 11년만에 두 정상의 만남.
* 많은 국민들의 뜨거운 관심.
* 뭔가 다가온듯한.. 통일..? 
* 과연 국민들의 생각은? 

### 2. 알고 싶은 것
* 각종 커뮤니티에서의 통일에 대해 글을 올리는 사람들에 대한 형태(본인 의견 or 단순 정보제공)
* 의견이라면 통일애대해 긍정적 의견인가? 부정적 의견인가? 

### 3. 결과 얻기 위한 사고
* 크게 두 가지 과정을 통해 원하는 결과를 얻을 수있다.

	1. 통일과 관련된 커뮤니티 글들을 수집한다(ex.Twiter or Facebook)
		1. 통일 이라는 키워드로만 검색하는 것은 데이터 양이 적고 다양한 통일관련 데이터를 얻기 힘듬으로 통일과 **의미상 연관**있는 단어들을 추출해야한다.

	2. 크롤링한 데이터를 가지고 긍정, 부정, 정보를 구분해낸다.


### 4. 기술적 적용 방법
* word2Vecotor,감정사전 score분석 등을 이용한다.

	1. word2Vecotor
		1. 단어끼리에 유사도는 비선형적인 데이터인데 이를 컴퓨터상에서 사용하기 위해 벡터형태로 분류하고 의미가 가까울수록 벡터 거리값이 가까워질 수있도록 설계되어있다.
		2. 통일을 선 검색하여 나온 단어를 konlpy등의 형태소 분석기로 분석한후 Word2Vector를 이용하여 해당 글에서 통일과 관련된 단어별 연관도를 추출해낸다. 

	2. 감정사전 이용
		1. 긍정/ 부정 사전을 이용하여 토큰화된 단어가 긍정사전에 있으면 스코어 +주고 부정사전에 있으면 -를 줍니다.
		2. 해당 글이 긍정인지 부정인지 score로 나타내도록 한다.

			 관련코드 	

```
# Word2Vec embedding
from gensim.models import Word2Vec
# tokenized_contents: 형태소분석기로 분석된 값
# size: 벡터 스페이스 
# min_count: 출현빈도가 50번 미만인 단어는 분석 제외
# window: 주변단어는 앞 뒤로 두개까지
# workers: cpu사용 갯수
# iter: 100번 반복 학습
# sg: CBOW/Skip-gram 두가지 모델중 두번째꺼 사용해라
embedding_model = Word2Vec(tokenized_contents, size=100, window = 2, min_count=50, workers=4, iter=100, sg=1)

# 통일관련 가장 유사한 단어들이 100개 출력됨
print(embedding_model.most_similar(positive=["통일"], topn=100))
```
### 4.5 기술개발 환경
* macOS
* python 3.5
* jupyter


### 5. 최종 결과 예상
#### input 
* 통일

#### process 
1. 데이터 모으기
	* 통일과 관련 된 언어 추출 : ex)정상회담,이산가족, 동독,서독 
	* 수동 검열을 통해 의미있는 검색 추출: ex)정상회담,이산가족
	* 다시 관련 글 검색 및 수동검열
	* 모든 통일 관련 데이터 저장
2. 데이터 판단
	* 저장된 데이터를 형태소분석하여 긍정인지 부정인지 판단.

#### output 
1. 모든 글 중 통일에 관한 긍정 부정 비율이 얼마나 되는지 수치로 보여줌.
2. 커뮤니티별로 통일에 관한 긍정 부정 비율이 얼마나 되는지 수치로 보여줌.
3. 통일과 연관된 단어들 각 긍정 부정 비율이 얼마나 되는지 수치로 보여줌.
4. 특정 비율에 해당 글들을 분류하여 보여줌.


### +6. 확장(시간적으로 가능하다면..)
1. 통일뿐 아니라 '특정' 단어와 연관된 단어를 커뮤니티별로 자동 탐색하여 보다 넓게 검색할 수 있는 '단어별 SNS 감정 판단 플랫폼'으로 확장시킬 수 있음. 



### 참고 링크

##### word2Vec 
* https://ratsgo.github.io/natural%20language%20processing/2017/03/08/word2vec/
* http://blog.theeluwin.kr/post/146591096133/%ED%95%9C%EA%B5%AD%EC%96%B4-word2vec

##### CBOW/Skip-gram 
* https://shuuki4.wordpress.com/2016/01/27/word2vec-%EA%B4%80%EB%A0%A8-%EC%9D%B4%EB%A1%A0-%EC%A0%95%EB%A6%AC/

###### 긍정/부정사전

* https://github.com/The-ECG/BigData1_1.3.3_Text-Mining/blob/master/dictionary.zip
		


