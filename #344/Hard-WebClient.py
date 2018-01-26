"""This module implements a very VERY simple command-line web client without any built in tools above the built-in socket module.
Currently only handles GET requests and HTTP/1.1, but has the option for expansion (see urlRequestBuild definition variables).
Does not handle any redirects, simply returns what is given.

Problem statement from www.reddit.com/r/dailyprogrammer.
Challenge #344 [Hard] Write a Web Client
https://www.reddit.com/r/dailyprogrammer/comments/7jzy8k/20171215_challenge_344_hard_write_a_web_client/

Submitted 1/26/2018
"""

__version__ = '0.0'
__author__ = 'Ilan Cohn'

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
