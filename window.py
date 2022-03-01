from tkinter import *
from main import *

stock1 = ""
stock2 = ""
history = ""
candle = ""

def btn_clicked():
    print("Button Clicked")
    stock1 = entry0.get()
    stock2 = entry2.get()
    history = entry1.get()
    candle = entry3.get()
    graph(stock1, stock2, history, candle)
    print(entry0.get() + " " +  entry1.get() + " " + entry2.get() + " " + entry3.get())


window = Tk()

window.geometry("1200x768")
window.configure(bg = "#2d283e")
canvas = Canvas(
    window,
    bg = "#2d283e",
    height = 768,
    width = 1200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    210.5, 335.0,
    image = entry0_img)

entry0 = Entry(
    bd = 3,
    bg = "#564f6f",
    highlightthickness = 0,

    )

entry0.place(
    x = 69, y = 303,
    width = 283,
    height = 62   
    )

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    210.5, 505.0,
    image = entry1_img)

entry1 = Entry(
    bd = 3,
    bg = "#564f6f",
    highlightthickness = 0)

entry1.place(
    x = 69, y = 473,
    width = 283,
    height = 62)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    931.5, 335.0,
    image = entry2_img)

entry2 = Entry(
    bd = 3,
    bg = "#564f6f",
    highlightthickness = 0)

entry2.place(
    x = 790, y = 303,
    width = 283,
    height = 62)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    931.5, 505.0,
    image = entry3_img)

entry3 = Entry(
    bd = 3,
    bg = "#564f6f",
    highlightthickness = 0)

entry3.place(
    x = 790, y = 473,
    width = 283,
    height = 62)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    496.5, 246.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 483, y = 603,
    width = 208,
    height = 100)

window.resizable(False, False)
window.mainloop()
