import sms
# from sms import *
import sqlite3
from datetime import datetime

conn=sqlite3.connect("recieved_messages1.db")
cur=conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS recieved_messages1 
(sender TEXT, recieved_time TEXT, content TEXT, state1 TEXT)""")
conn.commit()
conn.close()

print("made database")

def search(number="",recieved_time="" ,content="", state=""):
    global found
    found = True
    conn=sqlite3.connect("recieved_messages1.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM recieved_messages1 WHERE sender=? AND recieved_time=? AND content=? AND state1=?" , (str(number),str(recieved_time),str(content),str(state)))
    global rows
    rows=cur.fetchall()
    conn.close()
    if rows == []:
        found = False


def save_message():
    m = sms.Modem('/dev/ttyUSB0')
    msgs = m.messages()
    print(len(msgs))
    msgslen = len(msgs)
    i = 0
    while i < msgslen:
        print(i)
        
        global sent_date
        global sent_message
        global sent_sender
        sent_message = msgs[i].text
        sent_sender = msgs[i].number
        sent_date = msgs[i].date
        state0 = "recieved"
        search(number=sent_sender, recieved_time= sent_date, content=sent_message, state=state0)
        print(found)
        print(msgs[i].text)
        
        # if sent_message != "":
        if found == False:
            print(sent_message)
            conn=sqlite3.connect("recieved_messages1.db")
            cur=conn.cursor()
            cur.execute("INSERT INTO recieved_messages1 VALUES (?,?,?,?)",(sent_sender, sent_date, sent_message, state0))
            conn.commit()
            conn.close()       
            msgs[i].delete()
            search(number=sent_sender, recieved_time= sent_date, content=sent_message, state=state0)
            if found == True:
                print(found)
                print(i)
                msgs[i].delete()
        
        msgs[i].delete()
        search(number=sent_sender, recieved_time= sent_date, content=sent_message, state=state0)
        if found == True:
            msgs[i].delete()
        i = i + 1

    # a = 0
    # while i < msgslen:
    #     print(i)
    #     msgs[i].delete()
    #     a = a + 1


def send_sms(number ='', message = ''):
    modem = sms.Modem('/dev/ttyUSB0')
    message = 'hi'
    number = ""
    modem.send(number, message)
    if modem.ok == True:
        state0 = "sent"
        sent_date = datetime.now()
        conn=sqlite3.connect("recieved_messages1.db")
        cur=conn.cursor()
        cur.execute("INSERT INTO recieved_messages1 VALUES (?,?,?,?)",(number, sent_date, message, state0))
        conn.commit()
        conn.close()


save_message()
# send_sms()
