import web
from OSOM_server.resources import RESOURCES
from OSOM_server import utils
import json
import logging as log

level = log.INFO

_logfile = utils.get_logfile()

log.basicConfig(filename=_logfile,level=level,format='%(asctime)s %(levelname)s %(message)s')

urls = (
    '/',  'Root',
)

class Root(object):

    def publishable(self,item):
        if not isinstance(item,dict):
            return False
        req_keys = ['title','url','source']
        for key in req_keys:
            if key not in item:
                log("%s not in %r"%(key,item))
                return False
        return True

    def GET(self):
        """
        Scours RESOURCES for data samples, picks a
        random sample and publishes it
        """
        log.debug("Servicing GET request")
        resource = utils.pick_one_random_item(RESOURCES)
        if not resource:
            log.debug("No resource Found(1)")
            raise web.NotFound()
        item = resource.get_one()
        if self.publishable(item):
            log.debug("Publishing item")
            return json.dumps(item)
        log.warning("No publishable item found")
        raise web.NotFound()

class OSOMApp(web.application):
    def run(self,ip,port, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, (ip,port))

app = OSOMApp(urls,globals())

def start(ip='127.0.0.1',port=9000):
    log.info("Starting osom-api server")
    app.run(ip,port)
