import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.settimeout(2)

print("Pinging Server:\n")

sent = 0
received = 0
rtts = []

for i in range(4):
    try:
        sent += 1
        start = time.time()
        client.sendto(b"ECHO_REQUEST", ("localhost", 6006))
        data, _ = client.recvfrom(1024)
        end = time.time()

        received += 1
        rtt = (end - start) * 1000
        rtts.append(rtt)

        print(f"Reply from server: seq={i} time={rtt:.2f} ms")

    except:
        print(f"Request timed out: seq={i}")
    time.sleep(1)

print("\nPing statistics:")
print(f"Sent = {sent}, Received = {received}, Lost = {sent - received}")

if rtts:
    print(f"Minimum = {min(rtts):.2f} ms, Maximum = {max(rtts):.2f} ms, Average = {sum(rtts)/len(rtts):.2f} ms")
