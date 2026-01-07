import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.settimeout(2)

print("Simulated Traceroute to Server:\n")

for ttl in range(1, 10):
    try:
        start = time.time()
        client.sendto(str(ttl).encode(), ("localhost", 5005))
        data, _ = client.recvfrom(1024)
        end = time.time()

        msg = data.decode()

        if "TIME_EXCEEDED" in msg:
            router = msg.split()[1]
            print(f"{ttl}   {router}   {(end-start)*1000:.2f} ms")

        elif "DESTINATION_REACHED" in msg:
            dest = msg.split()[1]
            print(f"{ttl}   {dest}   {(end-start)*1000:.2f} ms  (Reached)")
            break

    except:
        print(f"{ttl}   Request Timed Out")
