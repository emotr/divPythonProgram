from tkinter import *

root = Tk()

myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="International Space Station")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

# Kan gjøres på en linje 
#myLabel1 = Label(root, text="Hello World!").grid(row=0, column=0)



root.mainloop()