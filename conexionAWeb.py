import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.w3.org', 80))

cmd = 'GET www.w3.org HTTP/1.0\r\n\r\n' .encode()
mysock.send(cmd)

recopila_datos = True
while recopila_datos == True:
    data = mysock.recv(512)
    if len(data)<1:
        recopila_datos = False
    
    print(data.decode())

mysock.close()



