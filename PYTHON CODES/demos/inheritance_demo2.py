#Constructors in Inheritance

class Mammals():
	def __init__(self,name,lives="Land"):
		self.name = name
		self.lives = lives

	def display(self):
		print("The " , self.name , "lives on" , self.lives)


class Land_Animals(Mammals):
	pass


#Overriding Super class Constructors and methods
class Water_animals(Mammals):
	def __init__(self,name,lives):
		self.name = name
		self.lives = lives

#Using super() method to call super class constructors and methods
class Water_animals2(Mammals):
	def __init__(self,name,lives):
		super().__init__(name)
		self.lives = lives
	
	def display(self):
		print("This is the child class method")
		
	def disp(self):
		super().display()


la = Land_Animals("Panda")
la.display()

wa = Water_animals("Whale", "Water")
wa.display()

wa2 = Water_animals2("Whale", "Water")
wa2.display()
wa2.disp()
