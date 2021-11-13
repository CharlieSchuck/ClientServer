import os
from _thread import *
import socket
# pip install PyDictionary -- in terminal
from PyDictionary import PyDictionary

dict = PyDictionary()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # (IPv4, TCP)
threads = 0

try:
    s.bind((socket.gethostname(), 1234))  # host, port
except socket.error as e:
    print(str(e))

s.listen(5)  # a queue of length 5.


def userClient(user):
    user.send(str.encode('Enter a word. '))
    while True:
        inString = user.recv(1024)
        outString = dict.meaning(inString.decode('utf-8'))
        if not inString:
            break
        user.send(bytes((str(outString)), "utf-8"))
    user.close()


while True:
    clientSocket, address = s.accept()
    print(f"Connection from {address} has been created.")
    start_new_thread(userClient, (clientSocket, ))
    threads = threads + 1
    print('Client number: ' + str(threads))
clientSocket.close()
s.close()
