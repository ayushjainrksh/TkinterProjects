from tkinter import *

window = Tk()

l1=Label(window,text="Title")
l1.grid(row=0,column=0)
l2=Label(window,text="Author")
l2.grid(row=0,column=2)
l3=Label(window,text="Year")
l3.grid(row=1,column=0)
l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

t1 = Entry()
t1.grid(row=0, column=1)

t2 = Entry()
t2.grid(row=0, column=3)

t3 = Entry()
t3.grid(row=1, column=1)

t4 = Entry()
t4.grid(row=1, column=3)

b1 = Button(text="View all")
b1.grid(row=2, column=3)
b2 = Button(text="Search entry")
b2.grid(row=3, column=3)
b3 = Button(text="Add entry")
b3.grid(row=4, column=3)
b4 = Button(text="Udate")
b4.grid(row=5, column=3)
b5 = Button(text="Delete")
b5.grid(row=6, column=3)
b6 = Button(text="Close")
b6.grid(row=7, column=3)

window.mainloop()
