from socket import *

def createServer():
    serversocket = socket(AF_INET,SOCK_STREAM)
    #creating a socket is like creating the phone not the phone call
    try:
        serversocket.bind(('localhost', 9000))
        serversocket.listen(5) # queue incoming calls
        while(1):
            (clientsocket, address) = serversocket.accept()
            #next line runs only if the phonecalls received

            rd = clientsocket.recv(5000).decode()
            pieces = rd.split("\n")
            if( len(pieces) > 0):
                print(pieces[0])

            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)
    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as exc:
        print("Error:\n")
        print(exc)

    serversocket.close()


""" OUTPUT:
Access http://localhost:9000
GET / HTTP/1.1
GET /favicon.ico HTTP/1.1
GET / HTTP/1.1
GET /favicon.ico HTTP/1.1

Shutting down...
 """

print('Access http://localhost:9000')
createServer()