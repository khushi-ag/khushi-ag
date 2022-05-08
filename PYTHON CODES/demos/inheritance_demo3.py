#Multiple inheritance with Method Resolution Order (MRO)
'''
class EmployeePer (object):
	def __init__ (self, name, DOB,ID):
		self.name = name
		self.DOB = DOB
		self.AdharID = ID
		
		
	
		print("Employee" , self.name , "with Adhar Id ", self.AdharID , "born on " , self.DOB)

class EmployeeProf(object):
	def __init__ (self,name,DOJ,EID):
		self.name = name
		self.DOJ = DOJ
		self.EID = EID
		
	
	
		print ("Employee" ,self.name  , "with employee id ", self.EID,  "joined on " , self.DOJ )
		
class Employee(EmployeePer,EmployeeProf ):
	def __init__ (self,name,DOB,ID):
		super().__init__(name,DOB,ID)
		
		
o = Employee("Ram", "23/07/1994", 456789)

		
#Method Resolution Order
class A(object):
	def disp (self):
		print("in A")
		super().disp()
	
class B (object):
	def disp(self):
		print ("in B")
		super().disp()
		
class C (object):
	def disp(self):
		print("in C")
		
		
class X (A,B):
	def disp(self):
		print("in X")
		super().disp()
		
class Y (B,C):
	def disp(self):
		print("in Y")
		super().disp()
		
class P (X,Y):
	def disp(self):
		print("in P")
		super().disp()
	

obj = P()
obj.disp()
	
	


A B C
x (A, B) , Y (B,c)
 P (x,Y)
	
'''	
#Polymorphism (Method Overloading)	
	
	
class Calculator(object):
	def add (self , a=None ,b=None,c=None):
		if (a!=None and b!= None and c!=None ):
			print("Sum1 is " , a+b+c)
		else:	
			print("Sum2 is ", a+b)
		
a = Calculator()
a.add(2,3)
a.add(2,3,4)
		
	
	
	
	
	
	

