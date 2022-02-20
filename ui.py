import tkinter as tk
from tkinter import *


root = Tk()
def submit():
    hi = 2

myLabel1 = Label(root, text = "Hello World")
myLabel2 = Label(root, text = "Heheheha")

myLabel1.grid(row=0, column=5)

myLabel2.grid(row=0, column=6)
root.mainloop()