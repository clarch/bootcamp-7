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

def find_max_min(Arr):
  max_, min_ = Arr[0], Arr[0]
  
  Min_Max = []
  for arr in Arr:
    if arr < min_:
      min_ = arr
    elif arr > max_:
      max_ = arr
  
  if min_ == max_:
    Min_Max.append(len(Arr))
    return Min_Max
  else:
  	Min_Max.append(min_)
  	Min_Max.append(max_)
  	return Min_Max

print find_max_min([4, 4, 4, 4, 4])
