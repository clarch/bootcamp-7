# PEP8
class Person:
	people_count = 0
	def __init__(self, name, age):
		self.name = name
		self.age = age
		Person.people_count += 1

	def __repr__(self):
		return "<{}, {}>".format(self.name, self.age)

	def say_hello(self):
		return "Hello, I'm {} and I am {} y/o".format(self.name, self.age)


h = Person('Joe', 5)
d = Person('Jill',25)
u = Person('Joan', 15)
print h.people_count 
print h.age
print d.say_hello()

a = [('Jane', 23), ('Joe', 50), ('Jackie', 34), ('Jacob', 78), ('Jee', 18), ('josh', 60)]
b = []

for name, age in a:
	person = Person(name, age)
	b.append(person)

for person in b:
	print person.say_hello()




		




