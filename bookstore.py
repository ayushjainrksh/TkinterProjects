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

title = StringVar()
t1 = Entry(window,textvariable=title)
t1.grid(row=0, column=1)

author = StringVar()
t2 = Entry(window,textvariable=author)
t2.grid(row=0, column=3)

year = StringVar()
t3 = Entry(window,textvariable=year)
t3.grid(row=1, column=1)

isbn = StringVar()
t4 = Entry(window,textvariable=isbn)
t4.grid(row=1, column=3)

b1 = Button(text="View all", width=12)
b1.grid(row=2, column=3)
b2 = Button(text="Search entry", width=12)
b2.grid(row=3, column=3)
b3 = Button(text="Add entry", width=12)
b3.grid(row=4, column=3)
b4 = Button(text="Update", width=12)
b4.grid(row=5, column=3)
b5 = Button(text="Delete", width=12)
b5.grid(row=6, column=3)
b6 = Button(text="Close", width=12)
b6.grid(row=7, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2,column=0, rowspan=6, columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2, column=2,rowspan=6)
list1.configure(yscrollcommand = sb1.set)
sb1.configure(command=list1.yview)

window.mainloop()
