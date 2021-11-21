from tkinter import *

root = Tk()
root.title("Enkel kalkulator") # Setter på en tittel på vinduet

# Input feltet
e = Entry(root, width=50, borderwidth=5, bg="#dcdcdc")
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10) 

# Lar bruker skrive inn tall med knapper
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

# Fjerner input
def button_clear():
    e.delete(0, END)

# Addisjon
def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number) 
    e.delete(0, END)

# Likhetstegn. Basert på hva som skal regnes ut
def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + float(second_number))
    if math == "subtraction":
        e.insert(0, f_num - float(second_number))
    if math == "multiplication":
        e.insert(0, f_num * float(second_number))
    if math == "division":
        if second_number == 0:
            e.insert(0, "Kan ikke dele på 0")
        else:
            e.insert(0, f_num / float(second_number))

# Subtraherer
def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number) 
    e.delete(0, END)

# Multipliserer
def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number) 
    e.delete(0, END)

# Dividerer
def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number) 
    e.delete(0, END)

# Tar kvadratrot av et tall
def button_square_root():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)
    if f_num < 0:
        e.insert(0, "Kan ikke ta kvadratrot av et negativt tall")
    else:    
        e.insert(0, float(pow(f_num, 1/2)))

# Setter 10 ^ inputet tall. Feks input 2 gir 10^2
def button_ten_raised_to():
    number = e.get() 
    f_num = float(number)
    e.delete(0, END)
    e.insert(0, pow(10, f_num))

# TODO: fiks
# Legger til et komma så man kan bruke flyttall
def button_comma():
    number = e.get()
    e.delete(0, END)
    e.insert(0, float(number))

def first_parentheses():
    return

def second_parentheses():
    return

# Gjør inputet tall negativt
def button_negative():
    number = e.get()
    e.delete(0, END)
    number = float(number)
    e.insert(0, (number * -1))


# Definer knapper

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_equal = Button(root, text="=", padx=88, pady=20, command=button_equal)
button_clear = Button(root, text="clear", padx=79, pady=20, command=button_clear)
button_comma = Button(root, text=", ", padx=53, pady=20, command=button_clear)
button_negative = Button(root, text="(-)", padx=50, pady=20, command=button_negative)

button_first_parentheses = Button(root, text="(", padx=55, pady=20, command=first_parentheses)
button_second_parentheses = Button(root, text=")", padx=55, pady=20, command=second_parentheses)

button_subtract = Button(root, text="-", padx=41, pady=20, command=button_subtract)
button_multiply = Button(root, text="*", padx=41, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=41, pady=20, command=button_divide)
button_add = Button(root, text="+", padx=39, pady=20, command=button_add)

button_square_root = Button(root, text="square root", padx=21, pady=20, command=button_square_root)
button_ten_raised_to = Button(root, text="10^x", padx=40, pady=20, command=button_ten_raised_to)

# Sett knappene på skjermen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=6, column=1, columnspan=2)
button_equal.grid(row=4, column=1, columnspan=2)
button_comma.grid(row=3, column=3)
button_first_parentheses.grid(row=4, column=3)
button_second_parentheses.grid(row=5, column=3)
button_negative.grid(row=6, column=3)

button_add.grid(row=5, column=0)
button_subtract.grid(row=5, column=1)
button_multiply.grid(row=5, column=2)
button_divide.grid(row=6, column=0)
button_square_root.grid(row=1, column=3, columnspan=1)
button_ten_raised_to.grid(row=2, column=3)

root.mainloop()