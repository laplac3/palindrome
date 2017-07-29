def create_dic(word):
	
	dic = {}
	key = []

#creates dictionary
	for i in range(1,len(word)):

		if True == dic.has_key(word[i]):
			i+=1
 
		else:
			dic[word[i]] = 0
			key.append(word[i])


#counts letters in word stores the numb in the dic
	for k in range(0,len(dic)):
		
		for j in range(0,len(word)):
			
			if key[k] == word[j]:
				dic[key[k]] +=1
				j+=1
			
			else:
				j+=1

		k+=1

	return dic, key



#print create_dic('aabbbcsdkh###weofhqqqqqqqqqqqqqqqqqqqqqqqq')
