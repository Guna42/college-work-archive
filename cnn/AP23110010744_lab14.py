w=int(input("Enter Window Size: "))
n=int(input("Enter Total Frames: "))
frames=list(range(n))
i=0
while i<n:
    print("\nFrames Sent:",frames[i:i+w])
    for f in frames[i:i+w]:
        print("Sending Frame",f)
    x=input("Enter lost frame number or 'ok': ")
    if x!="ok":
        lost=int(x)
        print("ACK Lost for frame",lost,"→ Retransmitting...")
        print("Sending Frame",lost)
    else:
        print("All ACKs Received")
        i+=w
