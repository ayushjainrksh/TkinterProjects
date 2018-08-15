from tkinter import *
window = Tk()

def kgconvert():
    grams = str("%.3f" % (float(val.get())*1000.0)) + " grams"
    pounds = str("%.3f" % (float(val.get())*2.20462)) + " pounds"
    ounces = str("%.3f" % (float(val.get())*35.274)) + " ounces"

    t1.delete(1.0,END)
    t1.insert(END, grams)

    t2.delete(1.0,END)
    t2.insert(END,pounds)

    t3.delete(1.0,END)
    t3.insert(END,ounces)


window.geometry("450x100");

m1=Messages(window, text="Weight(in kg)")
m1.grid(row=0, column=0, sticky=W)

val = StringVar()
e1 = Entry(window, textvariable=val)
e1.grid(row=0, column=1)

b1 = Button(window,text="Convert",command=kgconvert)
b1.grid(row=0, column=2)

t1=Text(window,height=2,width=20)
t1.grid(row=1,column=0)

t2=Text(window,height=2,width=20)
t2.grid(row=1,column=1)

t3=Text(window,height=2,width=20)
t3.grid(row=1,column=2)


window.mainloop()
