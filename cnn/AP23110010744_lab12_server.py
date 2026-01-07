import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("localhost", 6006))

print("Ping Server Running...")

while True:
    data, addr = server.recvfrom(1024)
    reply = "ECHO_REPLY"
    server.sendto(reply.encode(), addr)
