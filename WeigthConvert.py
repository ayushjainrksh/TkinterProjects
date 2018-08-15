from tkinter import *
window = Tk()

def kgconvert():
    t1.insert(END,float(val.get())*1000.0)
    t2.insert(END,float(val.get())*2.20462)
    t3.insert(END,float(val.get())*35.274)


val = StringVar()
e1 = Entry(window, textvariable=val)
e1.grid(row=0, column=1)

b1 = Button(window,text="Convert",command=kgconvert)
b1.grid(row=0, column=2)

t1=Text(window,height=1,width=20)
t1.grid(row=1,column=0)

t2=Text(window,height=1,width=20)
t2.grid(row=1,column=1)

t3=Text(window,height=1,width=20)
t3.grid(row=1,column=2)


window.mainloop()
