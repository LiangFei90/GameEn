# GameServer.py

from socket import *
from time import ctime

HOST = ''
PORT = '21567'
BUFSIZE = 1024
ADDR = (HOST,PORT)
NUM = 77

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(('',21567))
tcpSerSock.listen(5)

while True:
    print('waiting fro connection...')
    tcpCliSock,addr = tcpSerSock.accept()
    print('...connection form :'+str(addr))
    while True:
        data = tcpCliSock.recv(BUFSIZE).decode()
        if not data:
            break
        data = int(data)
        if data < NUM:
            message = 'Smaller'
        elif data > NUM:
            message = 'Biger'
        elif data == NUM:
            message = 'Bingo!!'

        tcpCliSock.send(('[%s] %s'%(ctime(),message)).encode())
        print([ctime()], ':', data)
tcpCliSock.close()
tcpSerSock.close()





