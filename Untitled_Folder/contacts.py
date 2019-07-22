from tkinter import *
import backend
import os
import sqlite3

# def open_contacts_command():
#     print("opening contacts")
backend.connect()


def search(First_name_text="",Surname_text="" ,contacts_number_text="", Staff_ID_text=""):
    global found
    found = True
    conn=sqlite3.connect("contacts.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM contacts WHERE people=? AND Surname=? AND contacts_number=? AND Staff_ID=?", (str(First_name_text),str(Surname_text),str(contacts_number_text),str(Staff_ID_text)))
    global rows
    rows=cur.fetchall()
    conn.close()
    if rows == []:
        found = False


def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    # print(selected_tuple[0])
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(First_name_text.get(),Surname_text.get(),contacts_number_text.get(),Staff_ID_text.get()):
        list1.insert(END,row)

def open_login(self):
        window.destroy()
        print('opening')
        os.system("python2 login_gui.py")

def open_messages():
    window.destroy()
    print('opening')
    os.system('python test_gui.py')

# def add_command():
#     search(First_name_text=First_name_text.get(),Surname_text=Surname_text.get() ,contacts_number_text=contacts_number_text.get(), Staff_ID_text=Staff_ID_text.get())
#     if found == False:
#         backend.insert(First_name_text.get(),Surname_text.get(),contacts_number_text.get(),Staff_ID_text.get())
#         list1.delete(0,END)
#         list1.insert(END,(First_name_text.get(),Surname_text.get(),contacts_number_text.get(),Staff_ID_text.get()))

# def delete_command():
#     backend.delete(selected_tuple[0])
#     list1.delete(0,END)
#     for row in backend.view():
#         list1.insert(END,row)

def update_command():
    backend.update(selected_tuple[0],First_name_text.get(),Surname_text.get(),contacts_number_text.get(),Staff_ID_text.get())

def open_main_menu():
    window.destroy()
    print('opening')
    os.system('python2 menu_gui.py')

window=Tk()

window.wm_title("Contacts")

l1=Label(window,text="First_name")
l1.grid(row=0,column=0)

l2=Label(window,text="Surname")
l2.grid(row=0,column=1)

l3=Label(window,text="contacts_number")
l3.grid(row=0,column=2)

l4=Label(window,text="Staff_ID")
l4.grid(row=0,column=3)

First_name_text=StringVar()
e1=Entry(window,textvariable=First_name_text)
e1.grid(row=1,column=0)

Surname_text=StringVar()
e2=Entry(window,textvariable=Surname_text)
e2.grid(row=1,column=1)

contacts_number_text=StringVar()
e3=Entry(window,textvariable=contacts_number_text)
e3.grid(row=1,column=2)

Staff_ID_text=StringVar()
e4=Entry(window,textvariable=Staff_ID_text)
e4.grid(row=1,column=3)

list1=Listbox(window, height=15,width=100)
list1.grid(row=8,column=0,rowspan=10,columnspan=5)

sb1=Scrollbar(window)
sb1.grid(row=3,column=5,rowspan=10)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)


# b3=Button(window,text="Add Contact", width=12,command=add_command)
# b3.grid(row=4,column=3)


b1=Button(window,text="Messages", width=12,command=open_messages)
b1.grid(row=14,column=6)

b2=Button(window, text = "Log In", width = 12, command = open_login)
b2.grid(row=15, column=6)

b3=Button(window,text="Main Menu", width=12,command=open_main_menu)
b3.grid(row=16,column=6)

b4=Button(window,text="Close", width=12,command=update_command)
b4.grid(row=17,column=6)

window.mainloop()
