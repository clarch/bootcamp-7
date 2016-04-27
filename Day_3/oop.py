from person import Person
# PEP8

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




		




