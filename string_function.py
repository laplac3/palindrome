#creates the first half of our list of paladromes

def string(dic,key):
	string = ''
	for k in range(0,len(key)):
		
		for i in range(0,dic[key[k]]):
			string = string + key[k]
			i+=1
		k+=1
					
	return string

#test
#print string({'a': 1, 'c': 1, 'b': 1},['a','b','c'])
