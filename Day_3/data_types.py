def data_type(x):
	'''
	Takes in an argument, x:
		- For a integer, return x ** 2
		- FOr a float, return x / 2
		- For a string, returns "hello" + string
		- For a boolean, return "boolean"
		- For a long, return squareroot(x)
	'''
	if type(x) == int:
		return x ** 2
	elif type(x) == float:
		return x / 2
	elif type(x) == str:
		return "Hello {}".format(x)
	elif type(x) == bool:
		return "boolean"
	elif type(x) == long:
		return "Long"
	else:
		return "Invalid entry"

print data_type(70)
print data_type(23.56)
print data_type("Princess")
print data_type(True)
print data_type(1000000000000)


