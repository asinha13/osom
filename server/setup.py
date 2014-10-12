from distutils.core import setup
import sys, subprocess

setup(name="osom-server",
      version="0.1",
      description="One Serving of Motivation: Server",
      author="Ambuj Sinha",
      author_email="ambujs.app@gmail.com",
      packages=['OSOM_server'],
      scripts=["bin/osom-server"],
      data_files=[
        ('/etc/nginx/conf.d/nginx-osom/',['nginx/conf.d/nginx-osom/nginx-osom-api.conf']),
        ('/etc/nginx/sites-enabled/',['nginx/sites-enabled/default']),
        ('/etc/init.d',['etc/init.d/osom-server'])
      ]
     )

LOGDIR = "/var/log/osom-server"

if "install" in sys.argv:
    subprocess.call(['mkdir','-p',LOGDIR])
    subprocess.call(['chown','admin:admin',LOGDIR])
    subprocess.call(['update-rc.d','osom-server','defaults'])
