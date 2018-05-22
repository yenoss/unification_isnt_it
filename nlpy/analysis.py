
from konlpy.tag import Kkma
from konlpy.utils import pprint
kkma = Kkma()

def getNounsList(sentence):	
	return kkma.nouns(sentence)
	