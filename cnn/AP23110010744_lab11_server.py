import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("localhost", 5005))

print("Traceroute Server Running...")

# Simulate 5 hops before 'destination'
hops = [
    "10.0.0.1",
    "10.0.0.2",
    "10.0.0.3",
    "10.0.0.4",
    "10.0.0.5"
]

while True:
    data, addr = server.recvfrom(1024)
    ttl = int(data.decode())

    if ttl <= len(hops):
        reply = "TIME_EXCEEDED " + hops[ttl-1]
    else:
        reply = "DESTINATION_REACHED 192.168.1.100"

    server.sendto(reply.encode(), addr)
