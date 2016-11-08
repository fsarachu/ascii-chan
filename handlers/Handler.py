import os

import webapp2
import jinja2


class Handler(webapp2.RequestHandler):
    def __init__(self):
        super().__init__()
        self._template_dir = os.path.join(os.path.dirname(__file__), '../templates')
        self._jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(self._template_dir), autoescape=True)

    def write(self, *args, **kwargs):
        self.response.write(*args, **kwargs)
