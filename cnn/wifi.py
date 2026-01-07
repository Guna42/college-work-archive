import psutil
for name, addrs in psutil.net_if_addrs().items():
    if "Wi-Fi" in name or "Wireless" in name:
        for a in addrs:
            if a.family == psutil.AF_LINK:
                print("Wi-Fi MAC:", a.address)
