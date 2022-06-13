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

    def sendFolders(self):
        folders=self.getFolders()
        for i in folders:
            folderPath = self.mainPath+"/"+i
            images,jsonFiles,pdfFileList = self.getFiles(folderPath)
            while True:
                data, addr = self.sock.recvfrom(1024)
                data = data.decode('utf-8')
                if (data == "newFolder"):
                    self.sock.send(b'newFolderData')
                    while True:
                        data, addr = self.sock.recvfrom(1024)
                        data = data.decode('utf-8')
                        if (data == "getImage"):
                            self.sendImage(folderPath, images)
                        if (data == "getPdf"):
                            self.sendPdfFiles(folderPath, pdfFileList)
                        if (data == "getJson"):
                            self.sendJsonFiles(folderPath, jsonFiles)
                        if( data=="completeFolder"):
                            break
                    break
        self.sock.send(b'completeAllFolders')

    def getFolders(self):
        self.mainPath = "C:/Users/PC/PycharmProjects/socketP/images"
        folders = os.listdir(self.mainPath)
        return folders

    def getFiles(self,folder):
        files = os.listdir(folder)
        images = []
        jsonFiles = []
        pdfFileList = []
        for i in files:
            if(i.endswith(".json")):
                jsonFiles.append(i)
            if (i.endswith(".png")):
                images.append(i)
            if (i.endswith(".jpg")):
                images.append(i)
            if (i.endswith(".jpeg")):
                images.append(i)
            if (i.endswith(".pdf")):
                pdfFileList.append(i)

        return images,jsonFiles,pdfFileList

    def sendPdfFiles(self,folderPath,fileList):
        for i in fileList:
            print(i)
            while True:
                data, addr = self.sock.recvfrom(1024)
                data = data.decode('utf-8')
                if (data == "next"):
                    self.sock.send(b'newData')
                    break
            filename = folderPath + "/" + i
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

    def sendJsonFiles(self,folderPath,fileList):
        for i in fileList:
            print(i)
            while True:
                data, addr = self.sock.recvfrom(1024)
                data = data.decode('utf-8')
                if (data == "next"):
                    self.sock.send(b'newData')
                    break
            filename = folderPath + "/" + i
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

    def sendImage(self,folderPath,fileList):
        for i in fileList:
            print(i)
            while True:
                data, addr = self.sock.recvfrom(1024)
                data = data.decode('utf-8')
                if (data == "next"):
                    self.sock.send(b'newData')
                    break
            filename = folderPath+"/"+i
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
            if(data == 'getFolders'):
                self.sendFolders()
