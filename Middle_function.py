#The middle function finds the odd entry of the dictionary and subtracts it by 1 then stores that letter as a variable midle

def middle(dic, key):
	
	for k in range(0,len(key)):
		
		if dic[key[k]] % 2 == 1:
			print 2 % dic['a'] != 0
			dic[key[k]]-=1
			middle_var = key[k]
			return middle_var, dic

		else:
			k+=1
	return '',dic
#test
#key = ['a','b','c']		
#dic = {'a':2, 'b':4,'c':4,}
#print middle(dic,key)


