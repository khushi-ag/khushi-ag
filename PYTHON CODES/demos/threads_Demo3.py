from threading import *
from time import *

class Railway:

	def __init__(self, available):
		self.available = available
		#create a lock
		self.l = Lock()


	#a method that reserves berth
	def reserve (self, wanted):
		#lock the current object
		self.l.acquire()
		#display the number of available seats"
		print("Available no. of berth  = " , self.available)


		if (self.available >= wanted):
			#find the thread name
			name = current_thread().getName()
			
			#display the berth allocated to person
			print(wanted , "berths allocated fo ", name)

			#make time delay so that the ticket is permitted
			sleep(1.5)

			#decrease the no.of available
			self.available -= wanted
		else:
			#if available < wanted
			print("Sorry, no berth")
		self.l.release()

obj =Railway(2)


t1=Thread(target=obj.reserve, args=(2,))
t2=Thread(target=obj.reserve, args=(1,))


t1.setName("Riya")
t2.setName("Ram")

t1.start()
t2.start()

t1.join()
t2.join()







