from tkinter import *

root = Tk()

# lager en funksjon for hva som skal skje når knappen trykkes på
def myClick():
    myLabel = Label(root, text="I clicked a button!")
    myLabel.pack()

myButton = Button(root, text="Click me!", command=myClick) # tar ikke parentes på myClick her
#myButton = Button(root, text="Click me!", state=DISABLED) # gjør at knappen er synlig, men kan ikke brukes
#myButton = Button(root, text="Click me!", padx=[heltall], pady=[heltall]) # endrer størrelsen på knappen
#myButton = Button(root, text="Click me!", command=myClick, fg="[farge]") # endrer fargen på teksten på knappen
#myButton = Button(root, text="Click me!", command=myClick, bg="[farge]") # endrer fargen på selve knappen
myButton.pack()
root.mainloop()