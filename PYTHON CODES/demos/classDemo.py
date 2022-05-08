class Myclass:
	def display(self):
		print ("Hi")

myobj = Myclass()
myobj.x = 4
print(myobj.x)
myobj2 = Myclass()
#print(myobj2.x)


class AddrBook:
	def __init__(self,nm,ph):
		self.name = nm
		self.phone = ph
		print ("Created record for", self.name)
	
	def display(self):
		print("Name: " , self.name)
		print("Number : " , self.phone)

	def updateBook(self,newph):
		self.phone = newph
		print ("Updated record for",self.name)


Ram = AddrBook("Ram", 9090909090)
Ram.display()
Ram.updateBook(9898989898989)
Ram.display()


class AddrBookEmail(Myclass,AddrBook):
	def __init__(self,nm,ph,em):
		AddrBook.__init__(self,nm,ph)
		#super(AddrBook,self).__init__()
		self.email = em
		
	'''def display(self):
		print("Name: " , self.name)
		print("Number : " , self.phone)
		print("Email : " ,self.email)
	'''
	def updateEmail(self, newem):
		self.email = newem
		print ("Update email for " ,self.email)


Joe = AddrBookEmail("Joe",90890909090,"joe@glsict.org")
Joe.display()
Joe.updateBook(90890909898)
Joe.display()
	
#issubclass()
print(issubclass(AddrBookEmail,AddrBook))
#print( AddrBookEmail is AddrBook)
#print( AddrBook in AddrBook.__bases__)

#isinstance()
print(isinstance (Ram,AddrBook))
	
