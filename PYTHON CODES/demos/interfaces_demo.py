from abc import ABC, abstractmethod
class Shapes(ABC):
	def __init__(self,x,y):
		self.x = x
		self.y = y
	
	def area (self):
	  	print("the area is " , self.x * self.y)
	
	def perimeter(self):
		print ("the perimeter is " , 2*(self.x + self.y))
	
	@abstractmethod
	def volume(self):
		pass

class cube (Shapes):
	def __init__ (self , x,y,z):
		super().__init__(x,y)
		self.z = z
	
	def volume (self):
		print ("the volume is " , self.x * self.y * self.z)



c = cube(4,5,6)
c.area()
c.perimeter()
c.volume()
