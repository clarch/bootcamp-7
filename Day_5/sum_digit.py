def sum_digit(A):
	total = 0

	# create a list compression
	b = [str(i) for i in A]

	# create a string
	b ="".join(b)

	for i in b:
		total += int(i)