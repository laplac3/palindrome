#halfs the values of each key in a dictionary
def half(dic,key):
	

	
	for k in range(0,len(key)):
	
		dic[key[k]] = dic[key[k]]/2
		k+=1
		
	return dic

#print half({'a':2,'b':4},['a','b'])
