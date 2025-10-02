# Step-1 : import tkinter
from tkinter import *

# Step-2 : gui interaction
window = Tk()

# Step-3 : adding inputs

window.title("Simple")
window.geometry("250x50")

lable1 = Label(window, text = "mail")
lable2 = Label(window,text="password")
lable1.grid(row = 0, columm = 1)

# Step-4 : main loop
window.mainloop()
