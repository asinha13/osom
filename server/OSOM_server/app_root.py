import web
from OSOM_server.resources import RESOURCES
from OSOM_server import utils

urls = (
    '/',  'Root',
)

class Root(object):

    def publishable(self,item):
        if not isinstance(item,dict):
            return False
        req_keys = ['title','url','author']
        for key in req_keys:
            if key not in item:
                return False
        return True

    def GET(self):
        """
        Scours RESOURCES for data samples, picks a
        random sample and publishes it
        """
        resource = utils.pick_one_random_item(RESOURCES)
        if not resource:
            raise web.NotFound()
        item = resource.get_one()
        if self.publishable(item):
            return item
        raise web.NotFound()
