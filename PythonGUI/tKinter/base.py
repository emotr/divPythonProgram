from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Window title")
root.iconbitmap("images/1829007.ico")

def open():
    global my_img
    top = Toplevel()
    top.title("Second Window title")
    top.iconbitmap("images/1829007.ico")
    my_img = ImageTk.PhotoImage(Image.open("images/smonk.jpg"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="close window", command=top.destroy).pack()

btn = Button(root, text="Open second window", command=open).pack()




mainloop()