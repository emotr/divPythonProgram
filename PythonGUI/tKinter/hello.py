from tkinter import *

root = Tk()

# Lager en "merkelapp" (label) widget
myLabel = Label(root, text="Hello World!")
# Dytter den ut til skjermen
myLabel.pack()
# Kjører helt til programmet blir stoppet.

root.mainloop()