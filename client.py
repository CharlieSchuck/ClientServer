import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # (IPv4, TCP)
s.connect((socket.gethostname(), 1234))

lstring = input("enter a string.")
s.send(bytes(lstring, "utf-8"))
msg = s.recv(1024)
lstring = msg.decode("utf-8")
print(lstring[1:])

s.close()