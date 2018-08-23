from tkinter import *
import backend

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END, row)

def insert_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,title_text.get(),author_text.get(),year_text.get(),isbn_text.get())

# def update_command():
    # backend.update()

window = Tk()

l1=Label(window,text="Title")
l1.grid(row=0,column=0)
l2=Label(window,text="Author")
l2.grid(row=0,column=2)
l3=Label(window,text="Year")
l3.grid(row=1,column=0)
l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

title_text = StringVar()
t1 = Entry(window,textvariable=title_text)
t1.grid(row=0, column=1)

author_text = StringVar()
t2 = Entry(window,textvariable=author_text)
t2.grid(row=0, column=3)

year_text = StringVar()
t3 = Entry(window,textvariable=year_text)
t3.grid(row=1, column=1)

isbn_text = StringVar()
t4 = Entry(window,textvariable=isbn_text)
t4.grid(row=1, column=3)

b1 = Button(text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)
b2 = Button(text="Search entry", width=12, command=search_command)
b2.grid(row=3, column=3)
b3 = Button(text="Add entry", width=12, command=insert_command)
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
