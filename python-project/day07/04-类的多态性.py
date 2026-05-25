class Animal:
	print("我会这么叫：")
class Cat(Animal):
	def say(self):
		print("喵喵喵~~~~")
class Dog(Animal):
	def say(self):
		print("汪汪汪~~~~")
def set_animal_say(a:Animal):
	a.say()
set_animal_say(Dog())
set_animal_say(Cat())