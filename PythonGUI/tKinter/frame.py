from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to code at yeet.com')
root.iconbitmap('images/1829007.ico')


frame = LabelFrame(root, text="This is my Frame", padx=50, pady=50)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Don't click here!")
b2 = Button(frame, text="Or here!")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)
root.mainloop()