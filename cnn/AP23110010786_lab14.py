w=int(input("Window Size: "))
t=int(input("Total Frames: "))
frames=list(range(t))
p=0
while p<t:
    print("\nCurrently Transmitting:",frames[p:p+w])
    simulate=input("Enter lost frame number or 'ok': ")
    if simulate!="ok":
        lf=int(simulate)
        print("ACK not received for frame",lf,"→ Re-Send triggered")
        print("Re-Sending Frame",lf)
    else:
        print("All ACKs received… shifting window")
        p+=w
