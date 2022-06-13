import socket
import time
import os
TCP_IP = '192.168.1.109'
TCP_PORT = 4000
server = (TCP_IP, TCP_PORT)
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

mainFolder = "C:/Users/optof/PycharmProjects/socketProgram/Results"
if not os.path.exists(mainFolder):
    os.makedirs(mainFolder)


def getFolders():
    f = 0
    while True:
        s.sendto("newFolder".encode('utf-8'), server)
        data = s.recv(BUFFER_SIZE)

        if (data == b'newFolderData'):
            tempFolder = mainFolder+"/result"+str(f)
            if not os.path.exists(tempFolder):
                os.makedirs(tempFolder)
            f +=1
            s.sendto("getImage".encode('utf-8'), server)
            getImages(tempFolder)
            time.sleep(0.5)
            s.sendto("getJson".encode('utf-8'), server)
            getJson(tempFolder)
            time.sleep(0.5)
            s.sendto("getPdf".encode('utf-8'), server)
            getPdf(tempFolder)
            time.sleep(0.5)
            s.sendto("completeFolder".encode('utf-8'), server)
        if (data == b'completeAllFolders'):
            break








def getJson(path):
    count = 0
    while True:
        s.sendto("next".encode('utf-8'), server)
        data = s.recv(BUFFER_SIZE)
        if (data == b'newData'):
            recived_f = path+"/"+'imgt_thread' + str(count) + '.json'
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

def getPdf(path):
    count = 0
    while True:
        s.sendto("next".encode('utf-8'), server)
        data = s.recv(BUFFER_SIZE)
        if (data == b'newData'):
            recived_f = path+"/"+'imgt_thread' + str(count) + '.pdf'
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


def getImages(path):
    count = 0
    while True:
        s.sendto("next".encode('utf-8'), server)
        data = s.recv(BUFFER_SIZE)
        if (data == b'newData'):
            recived_f = path+"/"+ 'imgt_thread' + str(count) + '.png'
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

message = input("write 'getFolders' -> ")
# inputMessage = 'getFolders'
s.sendto(message.encode('utf-8'), server)
time1 = time.time()
getFolders()
time2 = time.time()

print(time2-time1)
print('Successfully get the file')
s.close()
print('connection closed')