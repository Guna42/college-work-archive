import socket
s=socket.socket()
s.connect(("localhost",8888))
msg="Hello Server"
s.send(msg.encode())
reply=s.recv(1024).decode()
print("Server Reply:",reply)
s.close()
