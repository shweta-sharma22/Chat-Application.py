# import socket
# import sys
# import time

# s=socket.socket()
# host=input(str("Please enter the host you want to connect to: "))
# port=1025

# try:
#     s.connect((host, port))
#     print("Connected to Host")
# except:
#     print("Connection Failed")

# while 1:
#     incoming_message = s.recv(1024)
#     incoming_message = incoming_message.decode()
#     print("Reply-> " , incoming_message)

# message=input(str("Enter your Message-> "))
# message=message.encode()
# s.send(message)

import socket
import sys
import time
import threading

def client_thread(connection, addr):
    print("Connection established with:", addr)

    while True:
        message = connection.recv(1024)
        if not message:
            break
        incoming_message = message.decode()
        print("Received from", addr, ":", incoming_message)

        reply_message = "Message received from " + str(addr) + ": " + incoming_message
        connection.send(reply_message.encode())

    connection.close()
    print("Connection closed with:", addr)

s = socket.socket()
host = socket.gethostname()
print("Your connection server is starting on", host)
port = 1025

s.bind((host, port))
print("Server is ready to accept connections.")

s.listen(5)
print("Listening for incoming connections...")

while True:
    connection, addr = s.accept()
    thread = threading.Thread(target=client_thread, args=(connection, addr))
    thread.start()
