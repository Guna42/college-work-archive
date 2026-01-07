import socket

s=socket.socket()
s.connect(("localhost",8888))
msg="Hello Server"
s.send(msg.encode())
print("Message Sent:",msg)
data=s.recv(1024).decode()
print("Reply From Server:",data)
s.close()
