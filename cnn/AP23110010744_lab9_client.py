import socket
c=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg="Hello UDP Server"
c.sendto(msg.encode(),("localhost",7777))
data,addr=c.recvfrom(1024)
print("Server Response:",data.decode())
c.close()
