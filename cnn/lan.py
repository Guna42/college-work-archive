import psutil
for name, addrs in psutil.net_if_addrs().items():
    if "Local Area Connection" in name:
        for a in addrs:
            if a.family == psutil.AF_LINK:
                print(f"{name} MAC:", a.address)
