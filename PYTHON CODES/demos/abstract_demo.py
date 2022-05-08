from abc import ABC, abstractmethod
import math

#meta class ABC of the module abc(abstract base class) 

class Myclass (ABC):
	@abstractmethod  #decorator
	def calculate (self,x):
		pass
	
	def perimeter(self,a,b):
		print("Perimeter is ", 2*(a+b))
		
class subclass (Myclass):
	def calculate (self , x):
		print("square of " , x , "is", x*x)
		
		
class subclass2 (Myclass):
	def calculate (self , x):
		print("cube of " , x , "is", x*x*x)		
		

class subclass3 (Myclass):
	def calculate (self , x):
		print("square root of " , x , "is", math.sqrt(x))		
		

obj1 = subclass()
obj1.calculate(5)
obj2 = subclass2()
obj2.calculate(5)
obj3 = subclass3()
obj3.calculate(5)


#example of concrete methods