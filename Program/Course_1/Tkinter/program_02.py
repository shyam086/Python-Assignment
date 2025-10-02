#  Basic modification using tkinter

# Step-1 : import tkinter
from tkinter import *

# Step-2 : gui interaction
window = Tk()

# Step-3 : adding inputs
window.title("My space")
inp = Label(window, text = "Hello world!")
inp.pack()

# Step-4 : main loop
window.mainloop()
