def funky(a, b):
	""" 
	"""
	if isinstance(a, dict) and isinstance(b, dict):
		print dict(a.items() + b.items())

	elif isinstance(a, (list, str)) and isinstance(b, (list, str)
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