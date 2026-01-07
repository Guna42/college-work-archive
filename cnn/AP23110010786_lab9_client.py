import socket

c=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg="Hello UDP Server"
c.sendto(msg.encode(),("localhost",7777))
print("Message Sent:",msg)
data,addr=c.recvfrom(1024)
print("Reply From Server:",data.decode())
c.close()
