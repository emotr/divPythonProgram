from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to code at yeet.com')
root.iconbitmap('images/1829007.ico')


TOPPINGS = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")
] 

pizza = StringVar()
pizza.set("Pepperoni")

for text, topping in TOPPINGS:
    Radiobutton(root,text=text, variable=pizza, value=topping).pack(anchor=W)

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()    


#r = IntVar()
#r.set("2")
#Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

#myLabel = Label(root, text=pizza.get())
#myLabel.pack()

myButton = Button(root, text="Click me!", command=lambda: clicked(pizza.get())).pack()

mainloop()