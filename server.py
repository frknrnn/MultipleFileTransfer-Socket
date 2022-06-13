import socket
import time
from threading import Thread
import os


TCP_IP = '192.168.1.109'
TCP_PORT = 4000
BUFFER_SIZE = 1024

class ClientThread(Thread):

    def __init__(self, ip, port, sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print(" New thread started for "+ip+":"+str(port))
        self.getFiles()

    def getFiles(self):
        self.mainPath = "C:/Users/PC/PycharmProjects/socketP/images"
        self.files = os.listdir(self.mainPath)

        self.images = []
        self.jsonFiles = []
        self.pdfFileList = []

        for i in self.files:
            if(i.endswith(".json")):
                self.jsonFiles.append(i)
            if (i.endswith(".png")):
                self.images.append(i)
            if (i.endswith(".jpg")):
                self.images.append(i)
            if (i.endswith(".jpeg")):
                self.images.append(i)
            if (i.endswith(".pdf")):
                self.pdfFileList.append(i)

    def sendPdfFiles(self):
        for i in self.pdfFileList:
            print(i)
            while True:
                data, addr = self.sock.recvfrom(1024)
                data = data.decode('utf-8')
                if (data == "next"):
                    self.sock.send(b'newData')
                    break
            filename = self.mainPath + "/" + i
            f = open(filename, 'rb')
            self.flagDataSending = True
            while self.flagDataSending:
                l = f.read(BUFFER_SIZE)
                while (l):
                    self.sock.send(l)
                    # print('Sent ',repr(l))
                    l = f.read(BUFFER_SIZE)
                if not l:
                    print("DataSending")
                    time.sleep(0.5)
                    self.sock.send(b'ok')
                    self.flagDataSending = False
                    f.close()
                    break
        print('finish')
        self.sock.send(b'finish')

    def sendJsonFiles(self):
        for i in self.jsonFiles:
            print(i)
            while True:
                data, addr = self.sock.recvfrom(1024)
                data = data.decode('utf-8')
                if (data == "next"):
                    self.sock.send(b'newData')
                    break
            filename = self.mainPath + "/" + i
            f = open(filename, 'rb')
            self.flagDataSending = True
            while self.flagDataSending:
                l = f.read(BUFFER_SIZE)
                while (l):
                    self.sock.send(l)
                    # print('Sent ',repr(l))
                    l = f.read(BUFFER_SIZE)
                if not l:
                    print("DataSending")
                    time.sleep(0.5)
                    self.sock.send(b'ok')
                    self.flagDataSending = False
                    f.close()
                    break
        print('finish')
        self.sock.send(b'finish')

    def sendImage(self):
        for i in self.images:
            print(i)
            while True:
                data, addr = self.sock.recvfrom(1024)
                data = data.decode('utf-8')
                if (data == "next"):
                    self.sock.send(b'newData')
                    break
            filename = self.mainPath+"/"+i
            f = open(filename, 'rb')
            self.flagDataSending = True
            while self.flagDataSending:
                l = f.read(BUFFER_SIZE)
                while (l):
                    self.sock.send(l)
                    # print('Sent ',repr(l))
                    l = f.read(BUFFER_SIZE)
                if not l:
                    print("DataSending")
                    time.sleep(0.5)
                    self.sock.send(b'ok')
                    self.flagDataSending=False
                    f.close()
                    break
        print('finish')
        self.sock.send(b'finish')
    def run(self):
        while True:
            data, addr = self.sock.recvfrom(1024)
            data = data.decode('utf-8')
            #print(data)
            if (data == "getImage"):
                self.sendImage()
            if (data == "getPdf"):
                self.sendPdfFiles()
            if(data == "getJson"):
                self.sendJsonFiles()



tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcpsock.listen(5)
    print("Waiting for incoming connections...")
    (conn, (ip, port)) = tcpsock.accept()
    print(conn)
    print(type(conn))
    print('Got connection from ', (ip, port))
    newthread = ClientThread(ip, port, conn)
    newthread.start()
    threads.append(newthread)


for t in threads:
    t.join()