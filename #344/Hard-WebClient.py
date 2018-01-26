import socket

def main():
    (protocol,host,URI,port) = parseURL(input("URL (including 'HTTP://'): "))
    while not all([protocol,host,URI,port]):
        print('Invalid URL!')
        (protocol,host,URI,port) = parseURL(input("URL (including 'HTTP://'): "))
    httpRequest = urlRequestBuild(URI,host)
    connSocket = socket.socket()
    connSocket.connect((host,port))
    connSocket.send(httpRequest)

    recData = connSocket.recv(4096)
    while recData:
        print(recData.decode())
        recData = connSocket.recv(4096)
    connSocket.close()


def parseURL(rawURL):
    try:
        (protocol,address) = (x for x in rawURL.split('/',maxsplit=2) if x)

        if protocol.lower() != 'http:':
            return (None,None,None,None)

        if ':' in address and '/' in address:
            (host,portURI) = address.split(':')
            (port,URI) = portURI.split('/',maxsplit=1)
            URI = '/' + URI
            port = int(port)
        elif '/' in address:
            (host,URI) = address.split('/',maxsplit=1)
            URI = '/' + URI
            port = 80
        elif ':' in address:
            (host,port) = address.split(':')
            port = int(port)
            URI = '/'
        else:
            host = address
            port = 80
            URI = '/'

    except:
        return(None,None,None,None)

    return(protocol,host,URI,port)

def urlRequestBuild(URI,host,httpType='GET', httpRev = 'HTTP/1.1'):
    httpRequest = httpType + ' ' + URI + ' ' + httpRev + '\r\nHost: ' + host + '\r\n\r\n'
    return httpRequest.encode()


if __name__ == '__main__':
    main()
