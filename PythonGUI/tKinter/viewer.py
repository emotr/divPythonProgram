from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to code at yeet.com')
root.iconbitmap('images/1829007.ico') # Må være en .ico fil

# Lagret i en submappe kalt images
my_img1 = ImageTk.PhotoImage(Image.open("images/chess.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/smonk.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/Herbert_West_002.png"))
my_img4 = ImageTk.PhotoImage(Image.open("images/Skjermbilde.PNG"))

image_list = [my_img1, my_img2, my_img3, my_img4]

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E) 

myLabel = Label(image=my_img1)
myLabel.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global myLabel
    global button_forward
    global button_back

    # Fjerner nåværende bilde
    myLabel.grid_forget() 

    myLabel = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    # Skru av forward knapp på siste bilde
    if image_number == 4:
        button_forward = Button(root, text=">>", state=DISABLED)

    # Oppdatere knapper på hvert nye bilde
    myLabel.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    # Oppdater status bar
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def back(image_number):
    global myLabel
    global button_forward
    global button_back

    # Fjerner nåværende bilde
    myLabel.grid_forget()
    
    myLabel = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    # Skru av back knapp på første bilde
    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    # Oppdatere knapper på hvert nye bilde
    myLabel.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    # Oppdater status bar
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


button_back = Button(root, text="<<", command=back, state=DISABLED)
button_forward = Button(root, text=">>", command=lambda: forward(2))
button_quit = Button(root, text="Exit Program", command=root.quit)

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)

status.grid(row=2, column=0, columnspan=3, sticky=W+E) # W er "west" og E er "east"

root.mainloop()