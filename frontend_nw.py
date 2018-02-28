from tkinter import *
import backend

def view_button():
    lb1.delete(0,END)
    for row in backend.view():
        lb1.insert(END,row)

def search_button():
    lb1.delete(0,END)
    for row in backend.search(e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get()):
        lb1.insert(END,row)

def insert_button():
    backend.insert(e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get())
    lb1.delete(0,END)
    lb1.insert(END,(e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get()))

def delete_button():
    backend.delete(selected_tuple[0])

def get_selected_row(event):
    global selected_tuple
    index=lb1.curselection()
    if index:
        selected_tuple=lb1.get(index[0])
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])

def update_button():
    backend.update(selected_tuple[0],e1_value.get(),e2_value.get(),e3_value.get(),e4_value.get())

window = Tk()
window.wm_title("Book_Index")

b1 = Button(window,text='View All',command=view_button)
b1.grid(row=2,column=3)
b1 = Button(window,text='Search Entry',command=search_button)
b1.grid(row=3,column=3)
b1 = Button(window,text='Add Entry',command=insert_button)
b1.grid(row=4,column=3)
b1 = Button(window,text='Update',command=update_button)
b1.grid(row=5,column=3)
b1 = Button(window,text='Delete',command=delete_button)
b1.grid(row=6,column=3)
b1 = Button(window,text='Close',command=window.destroy)
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

lb1.bind('<<ListboxSelect>>',get_selected_row)

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

window.mainloop()
