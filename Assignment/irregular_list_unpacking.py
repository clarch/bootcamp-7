find = [(60, 70, 90, 9),(4, 5),(20, 30, 50)]

for f in find:
	'''
	Function takes in a list a tuples with different lengths
	'''
	if len(f) == 1:
		print "x: {}:".format(*f)

	elif len(f) == 2:
		print "x: {}, y: {}".format(*f)

	elif len(f) == 3:
		print "x: {}, y: {}, z: {}".format(*f)
		
	else:
		print "Invalid Entry"