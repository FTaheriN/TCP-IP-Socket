import socket
import sys

HOST = '127.0.0.1'  # localhost
PORT = 65432        # Port to listen 

# Create a TCP/IP socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((HOST, PORT))
serverSocket.listen()

serverSocket.listen(1)  #listen to only one client at a time

while True:
    connectionSocket,addr = serverSocket.accept()
    line = connectionSocket.recv(1024)
    print("server printing: " line)
    connectionSocket.close()
