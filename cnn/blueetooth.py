import psutil
for name, addrs in psutil.net_if_addrs().items():
    if "Bluetooth" in name:
        for a in addrs:
            if a.family == psutil.AF_LINK:
                print("Bluetooth MAC:", a.address)
