import webapp2
import os
import json
import jinja2

current_jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        main_template = current_jinja_environment.get_template('templates/main.html')
        self.response.write(main_template.render())


app = webapp2.WSGIApplication([
    ('/', MainHandler),
])
