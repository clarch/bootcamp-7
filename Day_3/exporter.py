# global vars / not good practice
people = [
		('Joe', 90),
		('Janet', 75),
		('Brian', 67)
	]

def super_sum(*args):
	return sum(args)

def hello_again(name, age):
	return "I am {} and {} years old".format(name, age)

def max_min(A):
	'''
	Returns max value - min value
	'''
	# return max(A) - min(A)
	max_, min_ = A[0], A[0]

	for a in A:
		if a>max_:
			max_=a
		elif a>min_:
			min_=a
	return max_ - min_