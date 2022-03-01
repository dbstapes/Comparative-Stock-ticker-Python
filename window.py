from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1200x900")
window.configure(bg = "#2d283e")
canvas = Canvas(
    window,
    bg = "#2d283e",
    height = 900,
    width = 1200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    259.0, 434.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#564f6f",
    highlightthickness = 0)

entry0.place(
    x = 82, y = 390,
    width = 354,
    height = 87)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    940.0, 434.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#564f6f",
    highlightthickness = 0)

entry1.place(
    x = 763, y = 390,
    width = 354,
    height = 87)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    521.0, 208.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 496, y = 687,
    width = 208,
    height = 100)

window.resizable(True, True)
window.mainloop()
