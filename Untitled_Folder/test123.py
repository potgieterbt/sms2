import serial
import time

class TextMessage:
    def __init__(self, recipient="+27810394959", message="HI"):
        self.recipient = recipient
        self.content = message

    def setRecipient(self, number):
        self.recipient = number

    def setContent(self, message):
        self.content = message

    def connectPhone(self):
        self.ser = serial.Serial('/dev/ttyUSB0', 460800, timeout=5, xonxoff = False, rtscts = False, bytesize = serial.EIGHTBITS, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE)
        time.sleep(1)

    def sendMessage(self):
        self.ser.write('ATZ\r'.encode())
        print(self.ser.readline())
        time.sleep(1)
        self.ser.write('AT+CMGF=1\r'.encode())
        time.sleep(1)
        print(self.ser.readline())
        self.ser.write('''AT+CMGS="'''.encode() + self.recipient.encode() + '''"\r'''.encode())
        time.sleep(1)
        print(self.ser.readline())
        self.ser.write(self.content.encode() + "\r".encode())
        time.sleep(1)
        print(self.ser.readline())
        self.ser.write(chr(26).encode())
        time.sleep(1)
        print(self.ser.readline())
        print(self.ser.readline())
        print(self.ser.readline())
        print(self.ser.readline())
        print(self.ser.readline())
        print(self.ser.readline())
        print(self.ser.readline())
        print(self.ser.readline())


    def disconnectPhone(self):
        self.ser.close()

sms = TextMessage("+27810394959","HI")
sms.connectPhone()
sms.sendMessage() 
sms.disconnectPhone()
print("message sent successfully")