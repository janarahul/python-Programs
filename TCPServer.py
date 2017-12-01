from socket import *
serverPort=13000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ("server started")
while 1:
	Csocket,clientAddress = serverSocket.accept()
	msg= Csocket.recv(1024)
	modmsg = msg.upper()
	print(clientAddress)
	Csocket.send(modmsg)
	Csocket.close() 
