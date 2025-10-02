from tkinter import *

window = Tk()
window.geometry('500x500')
window.title("My Calculator")

# Entry Box
e = Entry(window, width=56, borderwidth=5)
e.place(x=0, y=0)

# When number or operator clicked, append to entry
def click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(num))

# Evaluate the expression
def equal():
    try:
        result = eval(e.get())
        e.delete(0, END)
        e.insert(0, result)
    except:
        e.delete(0, END)
        e.insert(0, "Error")

# Clear function
def clear():
    e.delete(0, END)

# Number Buttons
Button(window, text='1', width=12, command=lambda: click('1')).place(x=10, y=60)
Button(window, text='2', width=12, command=lambda: click('2')).place(x=80, y=60)
Button(window, text='3', width=12, command=lambda: click('3')).place(x=170, y=60)

Button(window, text='4', width=12, command=lambda: click('4')).place(x=10, y=120)
Button(window, text='5', width=12, command=lambda: click('5')).place(x=80, y=120)
Button(window, text='6', width=12, command=lambda: click('6')).place(x=170, y=120)

Button(window, text='7', width=12, command=lambda: click('7')).place(x=10, y=180)
Button(window, text='8', width=12, command=lambda: click('8')).place(x=80, y=180)
Button(window, text='9', width=12, command=lambda: click('9')).place(x=170, y=180)

Button(window, text='0', width=12, command=lambda: click('0')).place(x=80, y=240)

# Operator Buttons
Button(window, text='+', width=12, command=lambda: click('+')).place(x=10, y=240)
Button(window, text='-', width=12, command=lambda: click('-')).place(x=170, y=240)
Button(window, text='*', width=12, command=lambda: click('*')).place(x=10, y=300)
Button(window, text='/', width=12, command=lambda: click('/')).place(x=80, y=300)

# Equal and Clear Buttons
Button(window, text='=', width=12, bg="#00b894", fg="white", command=equal).place(x=170, y=300)
Button(window, text='Clear', width=12, bg="#d63031", fg="white", command=clear).place(x=10, y=350)

window.mainloop()
