#import urllib
#import re
#
#webpage = urllib.urlopen("http://www.python.org")
#
#text = webpage.read()
#m = re.search(r'<a href="([^"]+)" .*>FAQ</a>', text, re.IGNORECASE)
#print(m.group(1))
#urllib.urlretrieve("http://www.python.org", "/home/zahid/python_home.html")

#from SocketServer import TCPServer, StreamRequestHandler
#
#
#class Handler(StreamRequestHandler):
#    def handle(self):
#        addr = self.request.getpeername()
#        print('Got Connection from', addr)
#        self.wfile.write('Than you for connecting to server')
#
#
#server = TCPServer(('', 1234), Handler)
#server.serve_forever()

#from SocketServer import TCPServer, ForkingMixIn, StreamRequestHandler
#
#
#class Server(ForkingMixIn, TCPServer):
#    pass
#
#
#class Handler(StreamRequestHandler):
#
#    def handle(self):
#        addr = self.request.getpeername()
#        print('Got Connection from', addr)
#        self.wfile.write('Thank your for connecting')
#
#
#server = Server(('', 1234), Handler)
#server.serve_forever()

#from SocketServer import TCPServer, ThreadingMixIn, StreamRequestHandler
#
#
#class Server(ThreadingMixIn, TCPServer):
#    pass
#
#
#class Handler(StreamRequestHandler):
#    def handle(self):
#        addr = self.request.getpeername()
#        print "Got Connection from", addr
#        self.wfile.write('Thank you for connecting')
#
#
#server = Server(('', 1234), Handler)
#server.serve_forever()

#import socket
#import select
#
#s = socket.socket()
#
#host = socket.gethostname()
#port = 1234
#s.bind((host, port))
#
#s.listen(5)
#inputs = [s]
#
#while True:
#    rs, ws, es = select.select(inputs, [], [])
#    for r in rs:
#        if r is s:
#            c, addr = s.accept()
#            print('Got Connection from', addr)
#            inputs.append(c)
#        else:
#            try:
#                data = r.recv(1024)
#                disconnected = not data
#            except socket.error:
#                disconnected = True
#            if disconnected:
#                print(r.getpeername(), 'disconnected')
#                inputs.remove(r)
#            else:
#                print(data)
#

#from twisted.internet import reactor
#from twisted.internet.protocol import Protocol, Factory
#
#
#class SimpleLogger(Protocol):
#
#    def connectionMade(self):
#        print('Got connection from', self.transport.client)
#
#    def connectionLost(self, reason):
#        print(self.transport.client, 'disconnected')
#
#    def dataReceived(self, data):
#        print(data)
#
#
#factory = Factory()
#factory.protocol = SimpleLogger
#
#reactor.listenTCP(1234, factory)
#reactor.run()

from twisted.internet import reactor
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver


class SimpleLogger(LineReceiver):

    def connectionMade(self):
        print('Got Connection from', self.transport.client)

    def connectionLost(self):
        print(self.transport.client, 'disconnected')

    def lineReceived(self, line):
        print(line)


factory = Factory()
factory.protocol = SimpleLogger

reactor.listenTCP(1234, factory)
reactor.run()
