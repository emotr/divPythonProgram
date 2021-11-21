from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Window title")
root.iconbitmap("images/1829007.ico")

# Kan brukes for å åpne bilder, pdfer, python filer etc
# Her åpner den et bilde
def open():
    global my_img
    root.filename = filedialog.askopenfilename(
        initialdir="C:/Users/emotr/Desktop/divProgrammering/divPythonProgram/PythonGUI/tKinter/images", 
        title="Select A File", filetypes=(("jpg files", "*.jpg"), ("png files", "*.png")))

    myLabel = Label(root, text=root.filename).pack()

    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_img).pack()

btn = Button(root, text="Open File", command=open).pack()

mainloop()
