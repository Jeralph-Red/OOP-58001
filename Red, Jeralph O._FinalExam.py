from tkinter import *

window = Tk()
window.title("Find the Smallest number")
window.geometry("400x300+20+10")

def findSmallest():
    Red = []
    Red.append(eval(Cute2.get()))
    Red.append(eval(Cute3.get()))
    Red.append(eval(Cute4.get()))
    conOfSmallest.set(min(Red))

lbl1 = Label(window ,text="The Program that Finds the Smallest Number")
lbl1.grid(row=0, column=1, columnspan=2, sticky=EW)

lbl2 = Label(window, text="Enter the first number:")
lbl2.grid(row=1, column=0, sticky=W)

Cute2 = StringVar()
ent2 = Entry(window, bd=3, textvariable=Cute2)
ent2.grid(row=1, column=1)
lbl3 = Label(window, text="Enter the second number:")
lbl3.grid(row=2, column=0)

Cute3 = StringVar()
ent3 = Entry(window, bd=3, textvariable=Cute3)
ent3.grid(row=2, column=1)
lbl4 = Label(window, text="Enter the third number:")
lbl4.grid(row=3, column=0, sticky=W)

Cute4 = StringVar()
ent4 = Entry(window, bd=3, textvariable=Cute4)
ent4.grid(row=3, column=1)
btn1 = Button(window, text="Find the Smallest no.", command=findSmallest)
btn1.grid(row=4, column=1)
lbl5 = Label(window, text="The smallest number:")
lbl5.grid(row=5, column=0, sticky=W)

conOfSmallest = StringVar()
ent5 = Entry(window, bd=3, state="readonly", textvariable=conOfSmallest)
ent5.grid(row=5, column=1)


mainloop()