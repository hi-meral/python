def multi(X):
	total = 1
	for n in X:
		total *= n
		
	return total

y = (8, 2, 3, -1, 7)
print(multi(y))