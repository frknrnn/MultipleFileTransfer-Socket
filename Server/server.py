import socket
import time
from threading import Thread
import os
from serverClient import ClientThread

noConnectionFlag = False

'''
For JETSON NANO
import netifaces as ni

wlanFlag = False
try:
    ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
except:
    wlanFlag = True

if (wlanFlag == True):
    try:
        ip = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
    except:
        noConnectionFlag = True

'''

ip = '192.168.1.108'

if (noConnectionFlag != True):
    print(ip)
    TCP_IP = str(ip)
    TCP_PORT = 5000
    BUFFER_SIZE = 1024

    tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcpsock.bind((TCP_IP, TCP_PORT))
    threads = []
    tcpsock.listen(5)
    while True:
        print("Waiting for incoming connections...")
        (conn, (ip, port)) = tcpsock.accept()
        print(conn)
        print(type(conn))
        print('Got connection from ', (ip, port))
        newthread = ClientThread(ip, port, conn)
        newthread.start()
        threads.append(newthread)


