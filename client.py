import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # (IPv4, TCP)

try:
    s.connect((socket.gethostname(), 1234))
except socket.error as e:
    print(str(e))

serverOut = s.recv(1024)

while True:
    lstring = input("enter a word.")
    s.send(bytes(lstring, "utf-8"))
    serverOut = s.recv(8192)
    print(serverOut.decode('utf-8'))
s.close()