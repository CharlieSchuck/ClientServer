import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # (IPv4, TCP)
s.bind((socket.gethostname(), 1234)) # host, port

s.listen(5) # a queue of length 5.
# im not putting this into a loop because we're just doing it once.
clientsocket, address = s.accept() # if anyone tries to connect, accept -- client socket object, client's address.
print(f"Connection from {address} has been created.")

lstring = clientsocket.recv(1024)
clientsocket.send(bytes(((str)(lstring.upper())), "utf-8"))

clientsocket.close()
