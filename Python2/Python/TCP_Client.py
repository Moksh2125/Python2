import socket
host="192.168.104.99"
port=2000
Addr=(host,port)
client_socket=socket.socket()
client_socket.connect(Addr)
message=input("->")
while message!="":
    client_socket.send(message.encode())
    data=client_socket.recv(1024).decode()
    print("Received from server ->",data)
    message=input("->")
client_socket.close()
