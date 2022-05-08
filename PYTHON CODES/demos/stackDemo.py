class Stack:
	def __init__(self):
		self.stack = []
		
		
	def push(self,newdata):
		if newdata not in self.stack:
			self.stack.append(newdata)
			return True
			
		else:
			return False
			
	
	def peep(self):
		return self.stack [-1]
		
	def  pop2(self):
		
		if  len (self.stack) < 0:
			return("No items to pop")
		else:
			return(self.stack.pop())
			
	def disp_item(self):
		print(self.stack)

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.disp_item()
print("The item peep is ", s.peep())

item = s.pop2()
print("Item popped is ", item)
s.disp_item()
			
			
		
		