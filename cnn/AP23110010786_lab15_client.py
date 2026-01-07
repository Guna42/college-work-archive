import socket

cli=socket.socket()
cli.connect(("localhost",6060))
content=cli.recv(900000).decode()
new=open("output_received.txt","w")
new.write(content)
new.close()
print("File Successfully Received & Stored")
cli.close()
