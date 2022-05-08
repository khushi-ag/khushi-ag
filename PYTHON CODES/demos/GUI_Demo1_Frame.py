from tkinter import *

#create root window
root = Tk()

#give a title for root window
root.title ("My Frame")

#create a frame as child to root window
f = Frame (root, height = 400, width = 500, bg = "yellow", cursor = "cross")

#attach the frame on the root window
f.pack()

#let the root window wait for any event
root.mainloop()



