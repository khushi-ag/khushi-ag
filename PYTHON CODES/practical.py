# PY FILENAME.PY (in cmd)
'''
ASCII values: A-Z: 65-90, a-z: 97-122

sort() - for list, not for set
sorted()- returns the storted collection pass as a parameter. 

list[]
set{}
tuple()
dictionary{key and value pair}

#import the csv file.
import csv 

is-a : inheritance ; has-a : containership

#classs, data-member, data-function in py.
#fun insie class 'self' use as a parameter.

class Student:
	#constructor: __init__ -cannt be override
	def __init__(self):
		self.student_name= Name()

	def show_name(self):
		print(self.first)

stu.show_name()

stu.gender = "MALE"
print(stu.gender)
'''

#diff code:
class Name:
	def __init__(self):
		self.first=""
		self.middle=""
		self.last=""

	def get_first(self):
		return self.get_first
	
	def set_first(self,first):
		self.first = first

	def show(self):
		print(self.first, " ", self.middle, " ", self.last, " ")


class Person:
	#pass
	def __init__(self):
		self.name= Name()

	def get_name(self):
		return self.name

	def set_name(Self):
		self.name= set_name

	def show(self):
		self.name.show()

#completed a bl0g leave 2 blank lines-standard way.
class Student(Person):
	#pass
	def __init__(self):
		self.gender= ""

	def show(self):
		self.name.show()
		print(self.gender)

student1 = Student()
student1.name.set_first("fffff")
student1.name.middle= "MM"
student1.name.last= "ll"

student1.gender= "MALE"
student1.show()