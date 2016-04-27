# # Unpacking
# def hello(name, age, class_):
# 	'''
# 	Explans..
# 	'''
# 	if class_!='':
# 		return "I am{}, {} y/old, and {} class".format(name, age, class_)
# 	return "I am {} and I am {} old".format(name, age)

# people = [("Joe", 23, "high"),
# 		  ("Joe", 25, "Low"),
# 		  ("Mirriam", 89),
# 		  ("Maryann", 12)
# 		]

# # for person in people:
# # 	print hello(person[0], person[1])

# # for name, age in people:
# # 	print hello(name, age)

# for items in people:
# 	print hello(*items)

# args
# def super_sum(a, b, *args):
# 	'''
# 	Takes in variable number of items,
# 	and returns the sum.
# 	e.g super_sum(10, 20) = 30
# 		super_sum(10, 20, 30) = 70
# 		super_sum(1, 4, 5, 6, 7)
# 	'''
# 	total = 0
# 	for i in args:
# 		total += i

# 	return total
# print super_sum(10, 20)
# print super_sum(1, 4, 5, 6, 7)
# a =[10, 40, 60]
# print super_sum(*a)

# Kwargs
def hello_again(**kwargs):
	return "I am {} and I am {} old".format(kwargs['name'], kwargs['age'])

print hello_again(name='Joe', age=40)

other_people = [
				{'name': 'Jill', 'age':79},
				{'name': 'Jack', 'age':43},
				{'name': 'wham!', 'age':84}
			]

jill = {'name': 'Jill', 'age':79}
print hello_again(**jill)


	