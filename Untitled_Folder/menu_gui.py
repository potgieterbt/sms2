from tkinter import *
import sms_backend
import datetime as time
import os

# import login_gui



menu=Tk()

menu.wm_title("Basic Main Menu")

def open_messages():
    menu.destroy()
    print('opening')
    os.system('python2 test_gui.py')
    # os.system('python2 view_messaging_gui.py')
    # import view_messaging_gui

def open_contacts():
    menu.destroy()
    os.system('python2 contacts.py')
    print('opening')

def open_login():
    menu.destroy()
    print('opening')
    os.system("python2 login_gui.py")
    # import login_gui


b1=Button(menu,text="View Messages", width=25,command=open_messages)
b1.grid(row=5,column=3)

b2=Button(menu,text="View Contacts", width=25,command=open_contacts)
b2.grid(row=6,column=3)

b3=Button(menu,text="Login", width=25,command=open_login)
b3.grid(row=7,column=3)

l1 = Label(menu, text="NOTICE!")
l1.grid(row=1,column=3)

l2 = Label(menu, text="Login to write a new SMS and")
l2.grid(row=2,column=3)

l3 = Label(menu, text="to modify Contacts and Messages")
l3.grid(row=4,column=3)


menu.mainloop()
