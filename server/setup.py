from distutils.core import setup

setup(name="osom-server",
      version="0.1",
      description="One Serving of Motivation: Server",
      author="Ambuj Sinha",
      author_email="ambujs.app@gmail.com",
      packages=['OSOM_server'],
      data_files=[
        ('/etc/nginx/conf.d/nginx-osom/',['nginx/conf.d/nginx-osom/nginx-osom-api.conf']),
        ('/etc/nginx/sites-enabled/',['nginx/sites-enabled/default']),
      ]
     )
