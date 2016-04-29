class Animal(object):
	pass

class Person(object)
	def __init__(self, name, age, **kwargs):
		self.name = name
		self.age = age
	def walk(self):
		return "I am walking"

class Poacher(Person):
	def __init__(self, gun):
		Person.__init__(self, name, age, **kwargs)
		self.gun = kwargs.get('gun', 'AK-47')
		self.loc = kwargs.get('loc', 'Nairobi')
		self.game_park = kwargs.get('game_park', 'Mombasa')
		self.fav = kwargs.get('fav', 'Elephant')

		# print "Args",
		# args

		# # for args
		# if args[0]:
		# 	self.loc = args[0]
		# if args[1]:
		# 	self.gun = args[1]

class Tourist(object):
	pass

p = Person('Jane', 23)
pc = Poacher('Joe', 45, gun='riffle', game_park='NNP', loc='Mombasa')
pc = Poacher('Chris', 45, gun='colt', game_park='wha', loc='Bonoko')



