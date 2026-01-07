import socket
c=socket.socket()
c.connect(("localhost",5050))
data=c.recv(999999).decode()
f=open("received.txt","w")
f.write(data)
f.close()
print("File Received and Stored")
c.close()
