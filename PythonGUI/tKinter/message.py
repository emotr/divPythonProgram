from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Learn to code at yeet.com')
root.iconbitmap('images/1829007.ico')

# Forskjellige popupvinduer
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popupinfo():
    # Første tekststreng er navnet på popup vinduet og andre strengen er selve
    # teksten i vinduet
    response = messagebox.showinfo("This is my popup!", "Hello World!")
    Label(root, text=response).pack()

def popupwarning():
    response = messagebox.showwarning("This is a warning!", "Hello World!")
    Label(root, text=response).pack()

def popuperror():
    response = messagebox.showerror("This is an error!", "Hello World!")
    Label(root, text=response).pack()

def popupquestion():
    response = messagebox.askquestion("This is a question!", "Hello World!")
    Label(root, text=response).pack()
    if response == "yes":
        Label(root, text="You clicked yes!").pack()
    else:
        Label(root, text="You clicked no").pack()

def popupokcancel():
    response = messagebox.askokcancel("This is a question!", "Hello World!")
    Label(root, text=response).pack()

# for å gjøre noe med svaret på popupene med spørsmål eksempel:
def popupyesno():
    response = messagebox.askyesno("This is a question!", "Hello World!")
    Label(root, text=response).pack()
    if response == 1:
        Label(root, text="You clicked yes!").pack()
    else:
        Label(root, text="You clicked no").pack()


Button(root, text="Popupinfo", command=popupinfo).pack(anchor=W)
Button(root, text="Popupwarning", command=popupwarning).pack(anchor=W)
Button(root, text="Popuperror", command=popuperror).pack(anchor=W)
Button(root, text="Popupquestion", command=popupquestion).pack(anchor=W)
Button(root, text="Popupokcancel", command=popupokcancel).pack(anchor=W)
Button(root, text="Popupyesno", command=popupyesno).pack(anchor=W)


mainloop()