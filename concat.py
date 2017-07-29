#a function to concatinate the palidromes two ends, middle value and return an array containing the pallidroms

def con(array, middle):

	palidromes = []

	for i in range(0,len(array)):
		palidromes.append(array[i] + middle + array[i][::-1])
		#palidromes.append(array[i][::-1] + middle + array[i])
		i+=1
	return palidromes
	
#test
#print con(['abc','acb','cab'],'d')

