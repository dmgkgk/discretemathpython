def findit1(L): 
	for i in xrange(len(L)-1):
		if (L[i] > L[i+1]):
			return i

def findit2(L, a, b):
	if (b == a+2):
		if (L[a] > L[a+1]):
			return a
		if (L[a+1] > L[b]):
			return a+1
	if (b == a+1):
		return a
	mid = int((a+b)/2)
	if (L[a] > L[mid]):
		return findit2(L, a, mid)
	return findit2(L, mid+1, b)
