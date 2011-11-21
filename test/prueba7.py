
from twisted.internet import reactor, protocol
from twisted.internet.ssl import ClientContextFactory
from twisted.web.http import HTTPFactory

class QuickDisconnectProtocol(protocol.Protocol):
    def connectionMade(self):
        print "Connected to %s." % self.transport.getPeer().host
        self.transport.loseConnection()

class WebClientContextFactory(ClientContextFactory):
    def getContext(self, hostname, port):
        return ClientContextFactory.getContext(self)

class BasicClientFactory(HTTPFactory):

    def clientConnectionLost(self, connector, reason):
        print "Lost connection: %s" % reason.getErrorMessage()
        reactor.stop()

    def clientConnectionFailed(self, connector, reason):
        print "Connection failed: %s" % reason.getErrorMessage()
        reactor.stop()

contextFactory = WebClientContextFactory()
site = 'https://stream.connfu.com/connfu-stream-testing-emc2'
reactor.connectTCP(site, 443, BasicClientFactory(site))
reactor.run()
