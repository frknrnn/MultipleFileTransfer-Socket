import socket
import time
from threading import Thread
import os
from serverClient import ClientThread

TCP_IP = '192.168.1.109'
TCP_PORT = 4000
BUFFER_SIZE = 1024

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


