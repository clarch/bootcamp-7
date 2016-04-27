# Unpacking
def hello(name, age, class_):
	'''
	Explans..
	'''
	if class_!='':
		return "I am{}, {} y/old, and {} class".format(name, age, class_)
	return "I am {} and I am {} old".format(name, age)

people = [("Joe", 23, "high"),
		  ("Joe", 25, "Low"),
		  ("Mirriam", 89),
		  ("Maryann", 12)
		]

# for person in people:
# 	print hello(person[0], person[1])

# for name, age in people:
# 	print hello(name, age)

for items in people:
	print hello(*items)

	