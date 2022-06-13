import socket
import time

TCP_IP = '192.168.1.109'
TCP_PORT = 4000
server = (TCP_IP, TCP_PORT)
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))








def getJson():
    count = 0
    while True:
        s.sendto("next".encode('utf-8'), server)
        data = s.recv(BUFFER_SIZE)
        if (data == b'newData'):
            recived_f = 'imgt_thread' + str(count) + '.json'
            count += 1
            with open(recived_f, 'wb') as f:
                print('file opened')
                while True:
                    # print('receiving data...')
                    data = s.recv(BUFFER_SIZE)
                    # print('data=%s', (data))
                    # print(not data)
                    if (data == b'ok'):
                        print('file close()')
                        break
                    else:
                        f.write(data)
                    '''
                    if not data:
                        f.close()
                        print('file close()')
                        break
                    '''
                    # write data to a file
                f.close()
        elif (data == b'finish'):
            break

def getPdf():
    count = 0
    while True:
        s.sendto("next".encode('utf-8'), server)
        data = s.recv(BUFFER_SIZE)
        if (data == b'newData'):
            recived_f = 'imgt_thread' + str(count) + '.pdf'
            count += 1
            with open(recived_f, 'wb') as f:
                print('file opened')
                while True:
                    # print('receiving data...')
                    data = s.recv(BUFFER_SIZE)
                    # print('data=%s', (data))
                    # print(not data)
                    if (data == b'ok'):
                        print('file close()')
                        break
                    else:
                        f.write(data)
                    '''
                    if not data:
                        f.close()
                        print('file close()')
                        break
                    '''
                    # write data to a file
                f.close()
        elif (data == b'finish'):
            break


def getImages():
    count = 0
    while True:
        s.sendto("next".encode('utf-8'), server)
        data = s.recv(BUFFER_SIZE)
        if (data == b'newData'):
            recived_f = 'imgt_thread' + str(count) + '.png'
            count += 1
            with open(recived_f, 'wb') as f:
                print('file opened')
                while True:
                    # print('receiving data...')
                    data = s.recv(BUFFER_SIZE)
                    # print('data=%s', (data))
                    # print(not data)
                    if (data == b'ok'):
                        print('file close()')
                        break
                    else:
                        f.write(data)
                    '''
                    if not data:
                        f.close()
                        print('file close()')
                        break
                    '''
                    # write data to a file
                f.close()
        elif (data == b'finish'):
            break




message = input("-> ")
# inputMessage = 'getImage'
s.sendto(message.encode('utf-8'), server)
time1 = time.time()

getImages()
message = input("-> ")
# inputMessage = 'getJson'
s.sendto(message.encode('utf-8'), server)
getJson()
message = input("-> ")
# inputMessage = 'getPdf'
s.sendto(message.encode('utf-8'), server)
getPdf()

time2 = time.time()

print(time2-time1)
print('Successfully get the file')
s.close()
print('connection closed')