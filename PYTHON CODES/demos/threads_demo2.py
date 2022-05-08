from threading import *
'''
class MyThread (Thread):
	
	def __init__(self, name):
		Thread.__init__(self)
		self.name = name
	
	def run(self):
		print(self.name)

t1 = MyThread("Ram")
t11 = MyThread("Shyam")

t1.start()
t11.start()

t1.join()
t11.join()
		
'''


#Creating a Thread without creating sub class to Thread class

class MyThread2():
	
	def __init__(self, name):
		self.name = name

	def display(self, x, y):
		print(self.name)
		print("The argumnets provided are " , x, y)


obj = MyThread2("Ram")

t2 = Thread (target = obj.display, args = ("sita", "Geeta"))

t2.start()
			






