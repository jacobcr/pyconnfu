from twisted.internet.task import deferLater
from twisted.web.resource import Resource
from twisted.web.server import NOT_DONE_YET
from twisted.internet import reactor

class DelayedResource(Resource):
    def _delayedRender(self, request):
        request.write("<html><body>Sorry to keep you waiting.</body></html>")
        request.finish()

    def render_GET(self, request):
        d = deferLater(reactor, 5, lambda: request)
        d.addCallback(self._delayedRender)
        return NOT_DONE_YET

resource = DelayedResource()
