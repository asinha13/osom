from OSOM_server.resources_base import Resource
import json
from  OSOM_server import reddit_base as reddit
from  OSOM_server import utils
import logging as log

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
        return the top 500 posts from /r/getmotivated in json format
        """
        return "http://www.reddit.com/r/getmotivated.json?limit=500"

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
        if "imgur" not in post.get("domain"):
            return False
        # False if no url
        url = post.get('url')
        if not url:
            return False
        # False if album or gallery
        if '/a/' in url or '/gallery/' in url:
            return False
        return True

    def curate_url(self,url):
        if not url:
            return
        # loose test to make sure the url ends with an image extension
        last_part = url.split('/')[-1]
        sp = last_part.split('.')
        if len(sp) == 1:
            url += '.jpg'
        return url

    def get_one(self):
        resp = reddit.make_get_request(self.url)
        log.debug("Response from %s : %d"%(self.url,resp.status_code))
        if not resp.status_code == 200:
            return
        js = json.loads(resp.content)
        post_list = self.get_post_list(js)
        if not post_list:
            log.warning("No list obtained from %s"%(self.url))
            return
        for i in xrange(MAX_TRIES):
            post = utils.pick_one_random_item(post_list)
            post_data = post.get('data')
            if not post_data:
                continue
            if not self.publishable(post_data):
                continue
            img_url = self.curate_url(post_data.get("url"))
            if not img_url:
                continue
            return {"url" : img_url,
                    "source" : "http://www.reddit.com"+post_data.get("permalink")}

class REarthPorn(Resource):

    def _init(self):
        self.hits = 0

    @property
    def name(self):
        return "reddit_earthporn"

    @property
    def url(self):
        """
        return the top 500 posts from /r/earthporn in json format
        """
        return "http://www.reddit.com/r/earthporn.json?limit=500"

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
        if "imgur" not in post.get("domain"):
            return False
        # False if no url
        url = post.get('url')
        if not url:
            return False
        # False if album or gallery
        if '/a/' in url or '/gallery/' in url:
            return False
        return True

    def curate_url(self,url):
        if not url:
            return
        # loose test to make sure the url ends with an image extension
        last_part = url.split('/')[-1]
        sp = last_part.split('.')
        if len(sp) == 1:
            url += '.jpg'
        return url

    def curate_title(self,title):
        if not title:
            return
        try:
            while '[' in title:
                st = title.index('[')
                en = title.index(']')
                title = title[:st]+title[en+1:]
        except:
            pass
        return title

    def get_one(self):
        resp = reddit.make_get_request(self.url)
        log.debug("Response from %s : %d"%(self.url,resp.status_code))
        if not resp.status_code == 200:
            return
        js = json.loads(resp.content)
        post_list = self.get_post_list(js)
        if not post_list:
            log.warning("No list obtained from %s"%(self.url))
            return
        for i in xrange(MAX_TRIES):
            post = utils.pick_one_random_item(post_list)
            post_data = post.get('data')
            if not post_data:
                continue
            if not self.publishable(post_data):
                continue
            img_url = self.curate_url(post_data.get("url"))
            if not img_url:
                continue
            title = self.curate_title(post_data.get("title"))
            if not title:
                continue
            return {"subtitle" : title,
                    "url" : img_url,
                    "source" : "http://www.reddit.com"+post_data.get("permalink")}


RESOURCES = [
    REarthPorn(),
    RGetMotivaed()
]
