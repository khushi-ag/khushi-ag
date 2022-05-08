from threading import *

'''
print("Lets find the currently running thread", current_thread().getName())

if current_thread() == main_thread():
	print("The current thread is the Main thread")
else:
	print("The current thread is not main thread")




#Creating a thread without using a class
#Create  an object of Thread class and pass the function name as target for the thread as
#t = Thread(target = functionname , [args = (args1, args2, ....)]) and start the tread as t.start()

#from threading import Thread

def display():
	print("Hi")

for i in range (5):
	t = Thread(target = display)
	t.start()


def display2(str):
	print(str)
	
for i in range(5):
	t = Thread(target = display2 , args = ("hello",))
	t.start()


'''

#Creating a thread by creating a sub class to Thread class

class MyThread (Thread):
	
	#ovveride the run() method of the Thread class
	def run (self):
		for i in range (1,6):
			print (i)

#instantiate the class MyThread	
t1 = MyThread()


#start running the thread t1
t1.start()

#wait till the thread complete its execution
t1.join()







