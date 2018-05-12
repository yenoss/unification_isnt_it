import sys 
sys.path.append("../")

import unittest
from crawler import tweetCrawler 

class TestStringMethods(unittest.TestCase):

    def test_split(self):
        result = tweetCrawler.runCrawler("통일",4);        
        # 1페이지당 20개씩.
        self.assertEqual(len(result),20*4)    


if __name__ == '__main__':
    unittest.main()
