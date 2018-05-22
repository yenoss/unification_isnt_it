import sys 
sys.path.append("../")

import unittest
from crawler import tweetCrawler 
from nlpy import analysis

# 모든 라이브러리가 명확히 설치되었다면 해당 테스트가 원활하게 통과되어야합니다.
class TestModules(unittest.TestCase):

    def test_crawler_count(self):
        result = tweetCrawler.runCrawler("통일",2);        
        # 1페이지당 20개씩.
        self.assertEqual(len(result),20*2)    

    def test_nlpy_analysis(self):
        result = analysis.getNounsList("질문이나 건의사항은 깃헙 이슈 트래커에 남겨주세요.");                
        # 1페이지당 20개씩.
        self.assertEqual(result,['질문', '건의', '건의사항', '사항', '깃헙', '이슈', '트래커'])    





if __name__ == '__main__':
    unittest.main()
