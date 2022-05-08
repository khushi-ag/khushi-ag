#python program to create a push button and bind it with an event handler function

from tkinter import *

#method to be called when the button is clicked
def buttonClick(self):
	print("You have clicked me")


#create a root window
root = Tk()

#create a frame as a child to root window
f = Frame(root, height = 200, width = 300)

#let the frame will not shrink
f.propagate(0)

#attach the frame to root window
f.pack()

#create a push button as child to frame
b = Button (f, text = "Click Me...!", width = 15, height=2, bg = "yellow" ,fg = "blue" ,  activebackground = "green" , activeforeground = "red")




#attach button to the frame
b.pack()

#bind the left mouse button with the method to be called
b.bind("<Button-1>" , buttonClick)

#the root window handles the mouse click event
root.mainloop()



