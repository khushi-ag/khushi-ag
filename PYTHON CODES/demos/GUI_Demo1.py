from tkinter import *
from tkinter import font

#create the root window
root = Tk()

#set window Title
root.title("My Window")

#set window size
root.geometry("400x300")

#get all the supported font families
list_fonts = list(font.families())

print(list_fonts)
root.mainloop()
