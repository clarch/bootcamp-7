
def funky(a, b):
	""" 
	"""
	if isinstance(a, dict) and isinstance(b, dict):
		print dict(a.items() + b.items())

	elif (type(a) == type(b)) or ((type(a) == int and type(b) == float) or (type(a) == float and type(b) == int)):
		print a + b
	else:
		print 'Type Error, cannot concatenate'

c= 2
d = [3.4]
e = {1:'today',}
f = {2:'tommorrow'}

funky (c,d)
funky (e,f)
funky (c,f)

