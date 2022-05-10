from tkinter import *
class SemGrade:
    def __init__(self, win):
        self.lbl1=Label(win, text='Prelim:')
        self.lbl2=Label(win, text='Midterm:')
        self.lbl3=Label(win, text='Final:')
        self.lbl4=Label(win, text='Semestral Grade:')

        self.t1=Entry(bd=3)
        self.t2=Entry(bd=3)
        self.t3=Entry(bd=3)
        self.t4=Entry(bd=3)

        self.btn1 = Button(win, text='Add')
        self.b1 = Button(win, text='Compute for Semestral Grade', command=self.compute)
        self.b1.place(x=100, y=150)

        self.lbl1.place(x=70, y=50)
        self.t1.place(x=180, y=50)
        self.lbl2.place(x=70, y=80)
        self.t2.place(x=180, y=80)
        self.lbl3.place(x=70, y=110)
        self.t3.place(x=180, y=110)
        self.lbl4.place(x=70,y=190)
        self.t4.place(x=180,y=190)

    def compute(self):
        self.t4.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        num3=int(self.t3.get())
        result=(num1+num2+num3)/3   
        self.t4.insert(END, str(result))

window=Tk()
mywin=SemGrade(window)
window.title('Semestral Grade Calculator')
window.geometry("400x300+10+10")
window.mainloop()