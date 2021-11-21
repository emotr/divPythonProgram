from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Window title")
root.iconbitmap("images/1829007.ico")
root.geometry("400x400") # setter vindustørrelse

def slide():
    label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

# from har en _ mens to har ikke det
vertical = Scale(root, from_=0, to=400)
#.pack() må gjøres her på egen linje
vertical.pack()

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

label = Label(root, text=horizontal.get()).pack()

btn = Button(root, text="Click me to resize the window based on the slider values",
    command=slide).pack()


mainloop()