def computeInverse(L):
	result = []
	for x in L:
		result.append([x[1], x[0]])
	return result

def computeComposition(R, S):
	result = []
	for x in R:
		for y in S:
			if (y[1] == x[0]):
				temp = [y[0], x[1]]
				if (temp not in result):
					result.append(temp)
	return result

def isReflexive(L, n):
	for x in xrange(n):
		if ([x,x] not in L):
			return False
	return True
	
def isSymmetric(L):
	for x in L:
		if ([x[1], x[0]] not in L):
			return False
	return True
	
def isTransitive(L):
	for x in L:
		for y in L:
			if (x[1] == y[0]):
				if ([x[0], y[1]] not in L):
					return False
	return True	
	

def SymClosure(L):
	result = list(L)
	for x in L:
		if ([x[1],x[0]] not in L):
			result.append([x[1],x[0]])
	return result 
	
def RefClosure(L, n):
	result = list(L)
	for x in xrange(n):
		if ([x,x] not in L):
			result.append([x,x])
	return result 
	
def TransClosure(L):
	result = list(L)
	while(not isTransitive(result)):
		result.extend(computeComposition(result, L))
	return result
	

