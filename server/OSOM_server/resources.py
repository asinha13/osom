from OSOM_server.resources_base import Resource
import json
from  OSOM_server import reddit_base as reddit
from  OSOM_server import utils

MAX_TRIES = 10

class RGetMotivaed(Resource):

    def _init(self):
        self.hits = 0

    @property
    def name(self):
        return "reddit_getmotivated"

    @property
    def url(self):
        """
        return the top 100 posts from /r/getmotivated in json format
        """
        return "http://www.reddit.com/r/getmotivated.json?limit=100"

    def get_post_list(self,js):
        try:
            return js['data']['children']
        except:
            return

    def publishable(self, post):
        # False if NSFW
        if post.get("over_18"):
            return False
        # False if self post
        if post.get("is_self"):
            return False
        # False if domain not imgur
        if post.get("domain") != "i.imgur.com":
            return False
        # False if no url
        url = post.get('url')
        if not url:
            return False
        # False if album or gallery
        if '/a/' in url or '/gallery/' in url:
            return False
        return True

    def curate(self,url):
        if not url:
            return
        # loose test to make sure the url ends with an image extension
        last_part = url.split('/')[-1]
        sp = last_part('.')
        if len(sp) == 1:
            url += '.jpg'
        return url

    def get_one(self):
        resp = reddit.make_get_request(self.url)
        if not resp.status_code == 200:
            return
        js = json.loads(resp.content)
        post_list = _get_post_list(js)
        if not post_list:
            return
        for i in xrange(MAX_TRIES):
            post = utils.pick_one_random_item(post_list)
            if not self.publishable(post):
                continue
            img_url = self.curate(post.get("url"))
            if not img_url:
                continue
            return {"title" : post.get("title"),
                    "url" : img_url,
                    "author" : post.get("author")}

RESOURCES = [RGetMotivaed()]
