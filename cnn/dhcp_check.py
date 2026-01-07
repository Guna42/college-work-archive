import subprocess
out = subprocess.check_output("ipconfig /all", shell=True, text=True)
for line in out.splitlines():
    if "DHCP" in line:
        print(line.strip())
