class Person:
	'My class definition....Hello'
	noOfPerson = 0		#static data or  the class data
	def __init__(self,name,age=None):
		#Person.noOfPerson += 1
		Person.increment()
		self.name = name
		self.age = age
		return None
	
	@classmethod
	def increment(cls):
		cls.noOfPerson += 1
	
	@staticmethod
	def noofobjects():
		print("No. of person are",Person.noOfPerson)	

	def display(self):
		print("name : ", self.name)
		print("Age : ", self.age)

p = Person("Ram", 34)  #name = Ram and Age  = 34
p.display()
print("No. of person are",Person.noOfPerson)
p2 = Person("Shyam") #name = Shyam and Age= None
p2.display()
Person.noofobjects()

#types of instance methods

'''

Accessor methods   #getter methods
Mutators methods   #setter methods


#special class attributes

print(dir(Person))		#returns a list of object's attribute
print("Class Attributes", Person.__dict__)		#attributes of class with the values
print(Person.__name__)		#string name of the class
print(Person.__bases__)		#tuple of class Person's parent classes
print(Person.__module__)	#module where Person is defined
print(Person.__doc__)		#documentation of class Person	


#special Instance attributes

print(p.__class__)   #returns the name of class from which p is instantiated
print("Instance Attributes",p.__dict__)	#returns attributes of p
'''
