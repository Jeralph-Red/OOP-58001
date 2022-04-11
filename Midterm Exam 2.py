from tkinter import *
from tkinter import ttk
window = Tk()

def Name():
    txtfield['text'] = 'gg'

window.geometry("500x250+10+20")
window.title("Midterm in OOP")

label = Label(window, text="Enter your fullname: ", fg="red")
label.place(x=60, y=70)

txtfield = Entry(window, textvariable='gg', bd=7)
txtfield.place(x=270, y=65)

button = Button(window, text="Click to display your Fullname", fg="red", command=Name)
button.place(x=60, y=140)

txtfield = Entry(window, text = 'Name', bd=7)
txtfield.place(x=270, y=140)

window.mainloop()
