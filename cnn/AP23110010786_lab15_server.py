import socket

srv=socket.socket()
srv.bind(("localhost",6060))
srv.listen()
print("Server Active... Awaiting Client")
conn,addr=srv.accept()
file=open("data.txt","r")
conn.send(file.read().encode())
print("Transmission Completed")
file.close()
conn.close()
srv.close()
