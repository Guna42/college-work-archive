import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 7000))
server.listen(1)

print("Echo Server Started... Waiting for Client Connection...")

conn, addr = server.accept()
print("Connected to:", addr)

while True:
    data = conn.recv(1024).decode()

    if not data:
        break

    print("Client:", data)

    if data.strip().lower() == "exit":
        conn.send("exit".encode())
        break

    conn.send(data.encode())

conn.close()
server.close()
print("Server Closed.")
