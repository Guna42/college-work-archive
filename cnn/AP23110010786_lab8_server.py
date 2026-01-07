import socket

s=socket.socket()
s.bind(("localhost",8888))
s.listen(1)
print("TCP Server Waiting...")
c,addr=s.accept()
print("Client Connected")
data=c.recv(1024).decode()
print("Message From Client:",data)
c.send("Hello Client".encode())
c.close()
s.close()
