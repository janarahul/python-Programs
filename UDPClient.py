from socket import *
serverName = 'localhost'
serverPort = 12001
clientSocket = socket(AF_INET,SOCK_DGRAM)
message = raw_input('Input in lower case:')
clientSocket.sendto(message,(serverName,serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print (modifiedMessage)
clientSocket.close()

