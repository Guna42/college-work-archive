import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 7000))

while True:
    msg = input("Enter message: ")

    client.send(msg.encode())
    reply = client.recv(1024).decode()

    print("Echo from Server:", reply)

    if msg.strip().lower() == "exit":
        break

client.close()
print("Client Closed.")
