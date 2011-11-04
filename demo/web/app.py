import os
import sys

root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
web_dir  = os.path.join(root_dir, 'demo', 'web')
sys.path.insert(0, root_dir)

import cherrypy
from jinja2 import Environment, FileSystemLoader

from libcloud_monitoring.types import Provider
from libcloud_monitoring.providers import get_driver

env = Environment(loader=FileSystemLoader(os.path.join(web_dir, 'templates')))


class Root:

    def list_entities(self, username, apikey):
        driver = raxMon(username, apikey, ex_force_base_url="https://ele-api.k1k.me/v1.0")
        tmpl = env.get_template('list_entities.html')
        return tmpl.render()

    @cherrypy.expose
    def index(self):
        cookie = cherrypy.request.cookie
        if cookie.has_key('monitoring_username') and cookie.has_key('monitoring_apikey'):
            return list_entities(cookie['monitoring_username'], cookie['monitoring_apikey'])
        else:
            tmpl = env.get_template('index.html')
        return tmpl.render()


cherrypy.tree.mount(Root(), script_name='/')
cherrypy.config.update({'engine.autoreload_on': False})