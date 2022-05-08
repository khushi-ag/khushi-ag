#python program to create a push button and bind it with an event handler function

from tkinter import *

class MyButton:
	def __init__(self,root):
		#create a frame as a child to root window
		self.f = Frame(root, height = 200, width = 300)
		
		#let the frame will not shrink
		self.f.propagate(0)

		#attach the frame to root window
		self.f.pack()

		#create a push button as child to frame
		self.b = Button (self.f, text = "Click Me...!", width = 15, height=2, bg = "yellow" ,fg = "blue" ,  activebackground = "green" , activeforeground = "red", command = self.buttonClick)


		#attach button to the frame
		self.b.pack()

	#method to be called when the button is clicked
	def buttonClick(self):
		print("You have clicked me")


#create a root window
root = Tk()

#create an object to MyButton
mb = MyButton(root)





#the root window handles the mouse click event
root.mainloop()



