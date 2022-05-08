from tkinter import *

#create root window
root = Tk()

#create a canvas class as a child to root window
c = Canvas (root , bg = "blue", height = 700 , width = 1200 , cursor ='pencil')

#create a line on the canvas
id = c.create_line ( 50,50,200,50,200,150, width = 4 , fill = "white")

print(id)

#create an oval on the canvas
id = c.create_oval(100,100,400,300,width=5, fill="yellow", outline = "red", activefill = "green")

#create a polygon on the canvas
id = c.create_polygon (10,10,200,200,300,200, width =3, fill="green", outline = "red", smooth = 1, activefill ="lightblue")

#create a rectangle in the canvas
id = c.create_rectangle (500,200,700,600,width = 2,fill = "gray", outline = "black", activefill = "yellow")

#create some text on the canvas
fnt = ("Times", 40 , "bold italic underline")
id = c.create_text(500,100,text="My canvas",font = fnt, fill= "yellow" , activefill = "green")

file1 = PhotoImage(file = "/home/administrator/Desktop/Firefox_wallpaper.png")

#file2 = PhotoImage(file = "/home/administrator/Desktop/IMG-20190622-WA0006.png")


#display the image on the canvas in SE direction
id = c.create_image(500,200,anchor=SE, image =file1, activeimage = file1) 

#add canvas to the root window
c.pack()

#wait for any events
root.mainloop()



