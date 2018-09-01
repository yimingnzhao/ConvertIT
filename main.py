import webapp2
import os
import json
import jinja2
from data_objects import Unit
from seed_data import get_seed_data







current_jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        get_seed_data()
        main_template = current_jinja_environment.get_template('templates/main.html')
        self.response.write(main_template.render())


app = webapp2.WSGIApplication([
    ('/', MainHandler),
])
