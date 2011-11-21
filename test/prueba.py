from twisted.internet import reactor
from twisted.web.client import Agent
from twisted.web.http_headers import Headers

agent = Agent(reactor)

d = agent.request(
    'GET',
    'https://stream.connfu.com/connfu-stream-testing-emc2',
    Headers({'authorization': ['Backchat f2fc94294e373d67e9bd404fcc247f73']}),
    None)

def cbResponse(response):
    print 'Response received'
    print response.read()
d.addCallback(cbResponse)

def cbShutdown(ignored):
    reactor.stop()
d.addBoth(cbShutdown)

reactor.run()
