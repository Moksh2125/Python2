import socket
host=socket.gethostname()
port=2000
Addr=(host,port)
server_socket=socket.socket()
server_socket.bind(Addr)
server_socket.listen()
conn,addr=server_socket.accept()
print("Connection from ",str(addr))
while True:
    data=int(conn.recv(1024).decode())
    if not data:
        break
    conn.send(bytes(data*data).decode())
conn.close()
