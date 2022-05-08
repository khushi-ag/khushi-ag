class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
	

class SingleLinkedList:
	def __init__(self):
		self.head = None
	
		
	
	def traverse(self):
		i = self.head
		while i is not None:
			print(i.data)
			i = i.next
		
	def InsertAtBegin(self,newdata):
		newnode = Node(newdata)
		newnode.next = self.head
		self.head = newnode
		
		
		
		
		
		
	def InsertAtEnd(self,newdata):
		newnode = Node(newdata)
		if self.head == None:
			self.head = newnode
			return
		i = self.head
		while (i.next != None):
			i = i.next
		i.next = newnode
		
		
		
l = SingleLinkedList()
Node1 = Node(45)
l.head =Node1
Node2 = Node(67)
Node1.next = Node2
Node3 = Node(89)
Node2.next = Node3
l.traverse()
'''
Node4 = Node(10)
Node4.next = Node1
l.head = Node4
l.traverse()


Node5 = Node(10)
Node5.next = l.head
l.head = Node5
'''

l.InsertAtBegin(90)
l.traverse()

	
l.InsertAtEnd(1)
l.traverse()

	