from tkinter import *
import os

messaging=Tk()

messaging.wm_title("messaging")

def open_menu():
    messaging.destroy()
    print('opening')
    os.system('python2 menu_gui.py')
    # import view_messaging_gui

def open_contacts():
    messaging.destroy()
    print('opening')

def open_login():
    messaging.destroy()
    print('opening')
    os.system("python2 login_gui.py")
    # import login_gui

sender_text = StringVar()
e1 = Entry(messaging, textvariable = sender_text)
e1.grid(row= 2, column = 0)

date_time_text = StringVar()
e2 = Entry(messaging, textvariable = date_time_text)
e2.grid(row= 2, column = 1)


# state_text = StringVar()
# e3 = Entry(messaging, textvariable = state_text)
# e3.grid(row= 2, column = 2)

# content_text = StringVar()
# e4 = Entry(messaging, textvariable = content_text)
# e4.grid(row= 2, column = 3)
e4 = Text(messaging, height = 10, width = 25)
e4.grid(row = 2, rowspan = 2, column = 3, columnspan = 2)


t1 = Label(messaging, text = "Sender")
t1.grid(row=1, column = 0)

t2 = Label(messaging, text = "Date/Time")
t2.grid(row=1, column = 1)

t3 = Label(messaging, text = "State")
t3.grid(row=1, column = 2)

t4 = Label(messaging, text = "Message")
t4.grid(row=1, column = 3)

l1 = Listbox(messaging, height = 25, width = 70)
l1.grid(row = 3, rowspan = 15, column = 0, columnspan = 3)

b1=Button(messaging,text="Main Menu", width=25,command=open_menu)
b1.grid(row=15,column=3)

b2=Button(messaging,text="View Contacts", width=25,command=open_contacts)
b2.grid(row=16,column=3)

b3=Button(messaging,text="Login", width=25,command=open_login)
b3.grid(row=17,column=3)

state1 = StringVar()
state1.set("ALL")
d1 = OptionMenu(messaging, state1, "ALL", "Sent", "Recieved")
d1.grid(row = 2, column = 2)

state2 = StringVar()
state2.set("Sender")
d2 = OptionMenu(messaging, state2, "ALL", "Saved", "Unsaved")
d2.grid(row = 1, column = 0)

print(state1.get())

messaging.mainloop()