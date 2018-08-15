from tkinter import *
window = Tk()

def kgconvert():
    grams = str(float(val.get())*1000.0) + " grams"
    pounds = str(float(val.get())*2.20462) + " pounds"
    ounces = str(float(val.get())*35.274) + " ounces"

    t1.insert(END, grams)
    t2.insert(END,pounds)
    t3.insert(END,ounces)

m1=Message(window, text="Kg")
m1.grid(row=0, column=0)

# l1=Label(window, text="grams")
# l1.grid(row=1,column=1)
#
# l2=Label(window, text="pounds")
# l2.grid(row=1,column=3)
#
# l3=Label(window, text="ounces")
# l3.grid(row=1,column=5)

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
