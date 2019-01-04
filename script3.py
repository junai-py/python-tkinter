from tkinter import *
wd=Tk()
wd.title("GET STRING")
wd.geometry('1000x400')

lb=Label(wd,text=("ENTER YOUR NAME"),font=("Arial Black",50))
lb.grid(row=0)

txt=Entry(wd,width=30)
txt.grid(row=1,column=0)

def clicked():
    res=txt.get()
    lb.configure(text=res)
bt=Button(wd,text="click",width=20,command=clicked)
bt.grid(row=3,column=0)


wd.mainloop()