# Step-1 : import tkinter
from tkinter import *

# Step-2 : gui interaction
window = Tk()

# Step-3 : adding inputs

window.title("My space")
window.geometry("500x700")
window.config(background = "light blue")
frame1 = Frame(window, width=300, height=300, cursor="dot")
frame2 = Frame(window, width=300, height=300, cursor="dotbox")

button1 = Button(frame1, text="Button 1", bg = "blue")
button2 = Button(frame2, text="Button 2", bg = "green")
button3 = Button(frame1, text="Logged", fg = "red")

frame1.pack(side=TOP)
frame2.pack(side=BOTTOM)

button1.pack()
button2.pack()
button3.pack()

# Step-4 : main loop
window.mainloop()
