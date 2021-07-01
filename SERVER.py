import socket
import sys
import time

s=socket.socket()
host=input(str("Please enter the host you want to connect to: "))
port=1025

try:
    s.connect((host, port))
    print("Connected to Host")
except:
    print("Connection Failed")

while 1:
    incoming_message = s.recv(1024)
    incoming_message = incoming_message.decode()
    print("Reply-> " , incoming_message)

message=input(str("Enter your Message-> "))
message=message.encode()
s.send(message)