import socket
serverName='192.168.1.35'
serverPort=7070
clientSocket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = input('Insira uma sentença com letras minúsculas:')
print(str(message.encode()))
clientSocket.sendto(message.encode(encoding='ascii',errors='strict'),(serverName, serverPort))
modifiedMessage, serverAdress = clientSocket.recvfrom(1024)
print(modifiedMessage)
clientSocket.close()
