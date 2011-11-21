from twisted.python.log import err
from twisted.web.client import Agent
from twisted.internet import reactor
from twisted.internet.ssl import ClientContextFactory
from twisted.web.http_headers import Headers
from twisted.internet.protocol import Protocol

class BeginningPrinter(Protocol):
    def __init__(self, finished):
        self.finished = finished
        self.remaining = 1024 * 10

    def dataReceived(self, bytes):
        print bytes

    def connectionLost(self, reason):
        print 'Finished receiving body:', reason.getErrorMessage()
        self.finished.callback(None)


class WebClientContextFactory(ClientContextFactory):
    def getContext(self, hostname, port):
        return ClientContextFactory.getContext(self)

def display(response):
    print 'Response version:', response.version
    print 'Response code:', response.code
    print 'Response phrase:', response.phrase
    print 'Response headers:'
    print pformat(list(response.headers.getAllRawHeaders()))
    finished = Deferred()
    response.deliverBody(BeginningPrinter(finished))
    return finished

def main():
    contextFactory = WebClientContextFactory()
    agent = Agent(reactor, contextFactory)
    d = agent.request(
        'GET',
        'https://stream.connfu.com/connfu-stream-testing-emc2',
        Headers({'authorization': ['Backchat f2fc94294e373d67e9bd404fcc247f73']}),
        None)
    d.addCallbacks(display, err)
    d.addCallback(lambda ignored: reactor.stop())
    reactor.run()

if __name__ == "__main__":
    main()
