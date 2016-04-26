def super_sum(A):
	"""
		Takes in a list A:
		 - halves every even number 
		 - Doubles every odd number 
		and returns the sum of all.
	"""
	total = 0
	
	for i in A:
		if i % 2 == 0:
			total += (i / 2)
		else:
			total += (i * 2)

	return total

print super_sum([4, 3, 2, 1])


