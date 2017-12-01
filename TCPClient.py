from socket import *
serverName = "127.0.0.1"
serverPort = 13000
clientSocket=socket(AF_INET,SOCK_STREAM)
message = raw_input('Enter message:')
clientSocket.connect((serverName,serverPort))
clientSocket.send(message)
modmsg = clientSocket.recv(1024)
print (modmsg)
clientSocket.close()
