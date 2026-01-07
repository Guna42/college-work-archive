import psutil, socket
for name, addrs in psutil.net_if_addrs().items():
    print("Device:", name)
    for a in addrs:
        if a.family == socket.AF_INET: print(" IPv4:", a.address)
        elif a.family == psutil.AF_LINK: print(" MAC :", a.address)
    print()
