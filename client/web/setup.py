from distutils.core import setup
import os

def getallfiles(root):
    if os.path.isfile(root):
        return [root]
    if not os.path.isdir(root):
        return []
    ret = []
    for f in os.listdir(root):
        path = os.path.join(root,f)
        ret += getallfiles(path)
    return ret

def listdir(dst,sources):
    assert isinstance(sources,list)
    lst = []
    for source in sources:
        files = getallfiles(source)
        for f in files:
            dirpath = os.path.dirname(f)
            dstpath = os.path.join(dst,dirpath)
            lst.append((dstpath,[f]))

    return lst

setup(name="osom-web-client",
      version="0.1",
      description="One Serving of Motivation: Web Client",
      author="Ambuj Sinha",
      author_email="ambujs.app@gmail.com",
      data_files=[
        ('/etc/nginx/conf.d/nginx-osom/',['nginx/conf.d/nginx-osom/nginx-osom-static.conf']),
        ] + listdir("/var/osom/web/",["plugins","libraries"])
     )
