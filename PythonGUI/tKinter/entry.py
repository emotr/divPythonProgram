from tkinter import *

root = Tk()

e = Entry(root, width=50) # entry er et input felt
#e = Entry(root, width=[heltall]) # endrer størrelsen på feltet
#e = Entry(root, bg="[farge]", fg="[farge]") # endrer fargen på feltet og teksten
#e = Entry(root, borderwidth=[heltall]) # endrer størrelsen på grensen til feltet
e.pack()
#e.get() # e.get henter det som ble skrevet inn i feltet til e
e.insert(0, "Enter your name: ") # legger til default tekst i feltet. tallet er hvilket felt er

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Enter your name:", command=myClick) # tar ikke parentes på myClick her

myButton.pack()
root.mainloop()