# Step-1 : import tkinter
from tkinter import *

# Step-2 : gui interaction
window = Tk()

window.title("My space")
window.geometry("500x700")
window.config(background = "light blue")

# Step-3 : adding inputs
inp = Label(window, text = "Hello world!")
inp.pack()

# Step-4 : main loop
window.mainloop()
