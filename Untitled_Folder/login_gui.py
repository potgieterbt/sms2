from tkinter import *
import sms_backend
import datetime as time
import hashlib
import os

login=Tk()

login.wm_title("Login")

def open_menu():
    login.destroy()
    print('opening')
    os.system('python2 menu_gui.py')

def login_command():
    username = e1.get()
    password = hashlib.md5(e2.get().encode()).hexdigest()
    print(username, password)
    login.destroy()
    print('opening')
    os.system('python2 menu_gui_admin.py')


l1 = Label(login, text="Use your username and password to login!")
l1.grid(row=1,column=1, columnspan=2)

l2 = Label(login, text="Username")
l2.grid(row=2,column=1)

l3 = Label(login, text="Password")
l3.grid(row=3,column=1)

username_text = StringVar()
e1=Entry(login, textvariable = username_text)
e1.grid(row= 2, column = 2)

password_text = StringVar()
e2=Entry(login,show = "*", textvariable = password_text)
e2.grid(row= 3, column = 2)

b1 = Button(login, text = "Login", width = 15, command = login_command)
b1.grid(row = 4, column = 2)

b2=Button(login,text="Main Menu", width=12,command=open_menu)
b2.grid(row=4,column=1)

login.mainloop()
quit()