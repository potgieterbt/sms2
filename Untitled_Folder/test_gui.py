import sqlite3
from Tkinter import *
import os

# First create application class

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        # self.lbox_state= '', 'sent', 'recieved', 'recieved', 'sent', 'sent', 'sent', 'recieved', 'sent', 'recieved', 'recieved', 'sent'

        self.lbox_state = '', 'sent', 'recieved'

        self.conn=sqlite3.connect("test1.db")
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS test1 (name1 TEXT, state1 TEXT)")
        self.conn.commit()
        self.conn.close()
        # self.lbox_list = '', 'Adam', 'Lucy', 'Barry', 'Bob', 'Barry1', 'Barry2', 'James', 'Frank', 'Susan', 'Amanda', 'Christie'
        self.i = 0
        # for x in self.lbox_list:
        # while self.i <= 11:
        #     print(self.i)
        # self.y = self.lbox_list[self.i]
        self.state = self.lbox_state[self.i]
            
        #     print(self.y)
        #     print(self.state)
            
        self.found = True
        self.conn=sqlite3.connect("test1.db")
        self.cur=self.conn.cursor()
        # self.cur.execute("SELECT * FROM test1 WHERE name1=? AND state1=? ", (self.y, self.state))
        self.rows=self.cur.fetchall()
        # print(str(self.rows))
        self.conn.close()
        if self.rows == []:
            self.found = False

        #     if self.found == False:
        #         # for x in self.lbox_list:
        self.state = self.lbox_state[self.i]
        #         self.conn=sqlite3.connect("test1.db")
        #         self.cur=self.conn.cursor()
        #         # self.cur.execute("INSERT INTO test1 VALUES (?,?)", (self.y, self.state))
        #         self.conn.commit()
        #         self.conn.close()
        #             # self.i = self.i+1
        #     self.i = self.i+1


        self.pack()
        self.create_widgets()

    def open_menu(self):
        messaging.destroy()
        print('opening')
        os.system('python2 menu_gui.py')

    def open_contacts(self):
        messaging.destroy()
        print('opening')
        os.system('python2 contacts.py')

    def open_login(self):
        messaging.destroy()
        print('opening')
        os.system("python2 login_gui.py")

    # Create main GUI window
    def create_widgets(self):
        self.sender_text = StringVar()
        self.date_time_text = StringVar()
        self.date_time_text.trace("w", self.update_list)
        self.state1 = StringVar()
        self.state1.set("ALL")
        self.state2 = StringVar()
        self.state2.set("Sender")
        self.search_var = StringVar()
        self.search_var.trace("w", self.update_list)
        self.search_var1=StringVar()
        self.search_var1.set("ALL")
        self.search_var1.trace("w", self.update_list)
        self.content_text = StringVar()
        self.content_text.trace("w", self.update_list)


        self.entry1 = Entry(self, textvariable = self.search_var)
        self.entry2 = Entry(self, textvariable = self.date_time_text)
        # self.entry3 = Text(self, height = 10, width = 25)
        self.entry3 = Entry(self, textvariable = self.content_text)


        self.t1 = Label(self, text = "Sender")
        self.t2 = Label(self, text = "Date e.g. 2019-04-05")
        self.t3 = Label(self, text = "State")
        self.t4 = Label(self, text = "Message")

        self.lbox = Listbox(self, height = 25, width = 70)

        self.b1=Button(self,text="Main Menu", width=25,command=self.open_menu)
        self.b2=Button(self,text="View Contacts", width=25,command=self.open_contacts)
        self.b3=Button(self,text="Login", width=25,command=self.open_login)

        self.d1 = OptionMenu(self, self.search_var1, "ALL", "Sent", "Recieved")
        self.d2 = OptionMenu(self, self.state2, "ALL", "Saved", "Unsaved")



        self.entry1.grid(row= 2, column = 0)
        self.entry2.grid(row= 2, column = 1)
        # self.entry2.insert(0, "yyyy-mm-dd")
        self.entry3.grid(row = 2, rowspan = 2, column = 3, columnspan = 2)

        self.t1.grid(row=1, column = 0)
        self.t2.grid(row=1, column = 1)
        self.t3.grid(row=1, column = 2)
        self.t4.grid(row=1, column = 3)

        self.lbox.grid(row = 3, rowspan = 15, column = 0, columnspan = 3)

        self.d1.grid(row = 2, column = 2)
        self.d2.grid(row = 1, column = 0)

        self.b1.grid(row=15,column=3)
        self.b2.grid(row=16,column=3)
        self.b3.grid(row=17,column=3)



        # self.entry = Entry(self, textvariable=self.search_var, width=13)
        # self.lbox = Listbox(self, width=45, height=15)
        # self.label = Label(self, text="This is a test")


        # self.d1 = OptionMenu(self, self.search_var1, *self.lbox_state)

        # for item in self.lbox_list:
            # self.conn=sqlite3.connect("test1.db")
            # self.cur=self.conn.cursor()
            # self.cur.execute("CREATE TABLE IF NOT EXISTS test1 (name1 TEXT, state1 TEXT)")
            # self.cur.execute("SELECT * FROM test1 WHERE name1=? AND state1=? ", (self.y, str(self.lbox_state[1])))
            # lbox_list = self.cur.fetchall()
            # print(str(lbox_list))
            # self.conn.commit()
            # self.conn.close()

        self.conn=sqlite3.connect("test1.db")
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS test1 (name1 TEXT, state1 TEXT)")
        self.cur.execute("SELECT name1 FROM test1 ")
        # print(self.cur.fetchall())
        self.lbox_name = self.cur.fetchall()
        # print(str(self.lbox_name[5]).replace(",",""))
        self.cur.execute("SELECT state1 FROM test1 ")
        self.lbox_state1 = self.cur.fetchall()
        # print(str(self.lbox_state1[10]).replace(",",""))
        self.conn.commit()
        self.conn.close()      


        # self.entry.grid(row=1, column=0, padx=10, sticky='nsew')
        # self.lbox.grid(row=2, column=0, padx=10, sticky='nsew')
        # self.label.grid(row=0, column=0)
        # self.d1.grid(row= 3, column = 0)

        # self.columnconfigure(0, weight=1)
        # self.rowconfigure(0, weight=0)
        # self.rowconfigure(1, weight=0)
        # self.rowconfigure(2, weight=1)
        # Function for updating the list/doing the search.
        # It needs to be called here to populate the listbox.
        self.update_list()

    def update_list(self, *args):

        search_term = self.search_var.get()
        if self.search_var1.get() == "ALL":
            search_term1 = ""
        else:
            search_term1= self.search_var1.get()


        search_term2 = self.date_time_text.get()

        search_term3 = self.content_text.get()

        # print(self.search_var.get())
        # print(self.search_var1.get())


        # Just a generic list to populate the listbox
        # self.lbox_list = ['', 'Adam', 'Lucy', 'Barry', 'Bob', 'Barry1', 'Barry2',
        #              'James', 'Frank', 'Susan', 'Amanda', 'Christie']

        self.lbox.delete(0, END)

        a = 0
        
        for item in self.lbox_name:
            item=str(item).replace(",","").replace("(u'","").replace("')","").replace("('", "")
            lbox_content1= '', 'sent', 'recieved', 'recieved', 'sent', 'sent', 'sent', 'recieved', 'sent', 'recieved', 'recieved', 'sent', 'sent', 'sent'
            # abc = lbox_state[a]
            # print(self.lbox_state1[a])
            self.lbox_state = str(self.lbox_state1[a]).replace(",","").replace("(u'","").replace("')","").replace("('", "")
            # print(self.lbox_state)
                        
            # print(self.entry3.get("1.0",'end-1c'))
                
            if self.search_var1.get == "ALL":
                self.search_var1.set("")
                # print(search_term1)

            lbox_content = lbox_content1[a]

            if search_term.lower() in item.lower() and search_term1.lower() in self.lbox_state.lower() and search_term3 in lbox_content.lower():

                self.lbox.insert(END, item +"           "+self.lbox_state)
                # print(self.lbox_state)
            # elif search_term1.lower() in item.lower():
            #     self.lbox.insert(END, item)
            a = a + 1



messaging = Tk()
messaging.title('Messaging')
app = Application(master=messaging)
# print('Starting mainloop()')

messaging.resizable(False, False)

app.mainloop()
# messaging.mainloop()

# def search(number="",recieved_time="" ,content=""):
#     global found
#     found = True
#     conn=sqlite3.connect("recieved_messages1.db")
#     cur=conn.cursor()
#     cur.execute("SELECT * FROM recieved_messages1 WHERE sender=? AND recieved_time=? AND content=?", (str(number),str(recieved_time),str(content),))
#     global rows
#     rows=cur.fetchall()
#     conn.close()
#     if rows == []:
#         found = False
