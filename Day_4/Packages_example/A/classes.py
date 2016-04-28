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
		self.game = kwargs.get('game_park', 'Mombasa')
		self.fav = kwargs.get('fav', 'Elephant')

class Tourist(object):
	pass

p = Person('Jane', 23)
pc = Poacher('Joe', 45, gun='riffle')


