find = [(60, 70, 90, 9),(4, 5),(20, 30, 50)]

for f in find:
	if len(f) == 2:
		print "x: {}, y: {}".format(*f)
	elif len(f) == 3:
		print "x: {}, y: {}, z: {}".format(*f)
	else:
		print "Invalid Entry"