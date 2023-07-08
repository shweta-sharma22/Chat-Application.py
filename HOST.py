# import socket
# import sys
# import time

# s=socket.socket()
# host=socket.gethostname()
# print("Your connection server is starting on", host)
# port=1025

# s.bind((host, port))
# print("Server is ready to accept")

# s.listen(1)
# connection, addr=s.accept()
# print("Connection established to address: ", addr)

# while 1:
#     message = input(str("Enter your message:"))
#     message=message.encode()
#     connection.send(message)

#     incoming_message=connection.recv(1024)
#     incoming_message=incoming_message.decode()
#     print("Reply:", incoming_message)


import socket
import sys
import time
import threading

def receive_messages(s):
    while True:
        incoming_message = s.recv(1024)
        incoming_message = incoming_message.decode()
        if not incoming_message:
            break
        print("Reply ->", incoming_message)

host = input("Please enter the host you want to connect to: ")
port = 1025

try:
    s = socket.socket()
    s.connect((host, port))
    print("Connected to Host")
except:
    print("Connection Failed")
    sys.exit()

# Start a thread to receive messages from the server
receive_thread = threading.Thread(target=receive_messages, args=(s,))
receive_thread.start()

while True:
    message = input("Enter your Message: ")
    message = message.encode()
    s.send(message)
