#created student.py so: from filename(w/o .py) import classname 
from student import Student

s = Student()	#class obj.
s.setname("Ram")
s.setage(21)
s.getname()
s.getage()


class Stu_Marks(Student):	#another class extends student class
	def setmarks(self,marks):
		self.marks = marks
	
	def getmarks(self):
		print("The marks of ", self.name, "  is ", self.marks)


s1 = Stu_Marks()	#new class obj
s1.setname("Krishna")
s1.setage(20)
s1.getname()
s1.getage()
s1.setmarks(80)
s1.getmarks()
