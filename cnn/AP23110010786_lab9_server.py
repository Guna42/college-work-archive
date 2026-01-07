import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("localhost",7777))
print("UDP Server Ready...")
data,addr=s.recvfrom(1024)
print("Message From Client:",data.decode())
s.sendto("Hello UDP Client".encode(),addr)
s.close()
