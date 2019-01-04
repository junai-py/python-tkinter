from tkinter import *
wd=Tk()
wd.title("junai")
wd.geometry('500x500')
lb=Label(wd,text="hello",font=("Arial Black",50))
lb.grid(row=0,column=0)
def clicked():
    lb.configure(text="button was clicked")
bt=Button(wd,text="click",bg="red",fg="blue",command=clicked)
bt.grid(row=1)
wd.mainloop()    