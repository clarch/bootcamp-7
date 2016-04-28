def super_sum(*args):
	'''

	Returns a sum of numbers.
		e.g 
			super_sum() ==> 0
			super_sum(1, 2, 3) ==> 6
			super_sum("str") ==> 0
			super_sum([1, 2, 3]) ==> 6
			super_sum([10], [20], [30])
	'''
	total = 0

	if args:
		for a in args:			
			if type(a) == str:
				return 0
			if type(a) == list:
				total += sum(a)
			else:
				total += a

		return total
	return 0


	

	