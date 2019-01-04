from tkinter import *

windows= Tk()

b1=Button(windows,text="execute")
b1.grid(row=0,column=0)
e1=Entry(windows)
e1.grid(row=0,column=1)
t1=Text(windows)
t1.grid(row=4)


windows.mainloop()