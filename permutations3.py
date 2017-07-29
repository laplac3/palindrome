def perm(word, array, step = 0):
	
	#at the end of the string we will add the permutations to array
	if step == len(word) and "".join(word) not in array:
		#print "".join(word)
		word = "".join(word)
		array.append(word)
	
	#everything to the right needs to be swapped
	for i in range(step, len(word)):
		
		#string copy and stored in an array
		string_copy = [ char for char in word ]
		
		##swap current index with the step
		string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
		
		#recuraw on the portion of string not swaped 
		perm(string_copy, array, step + 1)
		
	return array

#array = []
#notarray = []
#perm('abcd',array)
#print array


