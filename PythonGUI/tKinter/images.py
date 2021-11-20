from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to code at yeet.com')
root.iconbitmap('C:/Users/emotr/Downloads/1829007.ico') # Må være en .ico fil

# Hvis bildet er i samme mappe som denne fila, trengs ikke stien å være med
my_img = ImageTk.PhotoImage(Image.open("C:/Users/emotr/Pictures/smonk.jpg"))
myLabel = Label(image=my_img)
myLabel.pack()









button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()








root.mainloop()