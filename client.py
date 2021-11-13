import socket
#pip install pysimplegui
import PySimpleGUI as gui

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # (IPv4, TCP)

try:
    s.connect((socket.gethostname(), 1234))
except socket.error as e:
    print(str(e))

serverOut = s.recv(1024)

while True:
    layout = [[gui.Text('Enter a Word: ', size = (15, 1)), gui.InputText()], [gui.Submit()], [gui.Button("Cancel")]]
    window = gui.Window('Word Window', layout)
    event, values = window.read()
    if event == "Cancel" or event == gui.WIN_CLOSED:
        break

    lstring = str(values[0])
    window.close()

    s.send(bytes(lstring, "utf-8"))
    serverOut = s.recv(8192)

    layout = [[gui.Text(serverOut.decode('utf-8'))], [gui.Button("OK")]]

    window = gui.Window(lstring, layout)

    while True:
        event, values = window.read()
        if event == "OK" or event == gui.WIN_CLOSED:
            break
    window.close()
s.close()