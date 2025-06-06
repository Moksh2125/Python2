import socket
host=socket.gethostname()
port=2000
Addr=(host,port)
client_socket=socket.socket()
client_socket.connect(Addr)
message=input("Number to be squared->")
while message!="":
    client_socket.send(message.encode())
    data=client_socket.recv(1024).decode()
    print("Squared Number:",data)
    message=input("Number to be squared->")
client_socket.close()
