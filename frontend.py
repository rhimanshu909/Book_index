from tkinter import *
import backend

window = Tk()

b1 = Button(window,text='View All',command=backend.view())
b1.grid(row=2,column=3)
b1 = Button(window,text='Search Entry',command=backend.search())
b1.grid(row=3,column=3)
b1 = Button(window,text='Add Entry',command=backend.insert())
b1.grid(row=4,column=3)
b1 = Button(window,text='Update',command=backend.update())
b1.grid(row=5,column=3)
b1 = Button(window,text='Delete',command=backend.delete())
b1.grid(row=6,column=3)
b1 = Button(window,text='Close',command=backend.close())
b1.grid(row=7,column=3)

l1 = Label(window,text='Title')
l1.grid(row=0,column=0)
l1 = Label(window,text='Author')
l1.grid(row=0,column=2)
l1 = Label(window,text='Year')
l1.grid(row=1,column=0)
l1 = Label(window,text='ISBN')
l1.grid(row=1,column=2)

lb1 = Listbox(window,height=6,width=50,)
lb1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)
lb1.config(yscrollcommand=sb1.set)
sb1.config(command=lb1.yview)

e1_value=StringVar()
e1 = Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)
e2_value=StringVar()
e2 = Entry(window,textvariable=e2_value)
e2.grid(row=0,column=3)
e3_value=StringVar()
e3 = Entry(window,textvariable=e3_value)
e3.grid(row=1,column=1)
e4_value=StringVar()
e4 = Entry(window,textvariable=e4_value)
e4.grid(row=1,column=3)

'''t1 = Text(window,height=1,width=20)
t1.grid(row=2,column=0)
t2 = Text(window,height=1,width=20)
t2.grid(row=2,column=1)
t3 = Text(window,height=1,width=20)
t3.grid(row=2,column=2)
'''

window.mainloop()
