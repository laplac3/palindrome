from create_dic_function2 import create_dic
from Middle_function import middle
from half_function import half
from string_function import string
from permutations3 import perm
from concat import con

def main(something):
	lists = []
	notlists = []
	mid = ''
	evendic = {}
	halfdic = {}
	halfpal = ''
	a = []
	paladromes = []
	
	dic, key = create_dic(something)
	(mid,evendic) = middle(dic,key)
	halfdic = half(evendic,key)
	halfpal = string(halfdic,key)
	a = perm(halfpal, a)
	paladromes = con(a,mid)
	return paladromes
	
print main('abcdefghijabcdefghij')
print len(main('abcdefghijabcdefghij'))
