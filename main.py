from tkinter import *
from tkinter import ttk
window = Tk()

window.geometry("500x300+10+20")
window.title("Main GUI")

button = Button(window, text="Button", fg="red", font=("Verdana", 16))
button.place(x=50, y=70)

label = Label(window, text="This is a label", fg="blue", bg="orange")
label.place(x=90, y=170)

txtfld = Entry(window, text="This is a text field", bd=5)
txtfld.place(x=210, y=170)

v1 = IntVar()
radiobutton = Radiobutton(window, text="Male", variable=v1, value=1)
radiobutton1 = Radiobutton(window, text="Female", variable=v1, value=2)
radiobutton.place(x=150, y=70)
radiobutton1.place(x=150, y=90)

v2 = StringVar()
v2.set('Student 1')
data = "Student 1", "Student 2", "Student 3"
combo = ttk.Combobox(window, values=data)
combo.place(x=60, y=10)

data = "Student 1", "Student 2", "Student 3"
lb = Listbox(window, height=3, selectmode="Multiple")
for num in data:
    lb.insert(END, num)
lb.place(x=210)

window.mainloop()