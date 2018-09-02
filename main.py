import webapp2
import os
import json
import jinja2
import time
from data_objects import Unit, UnitType
from seed_data import get_seed_data
from google.appengine.ext import ndb







current_jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #get general units
        get_seed_data()
        time.sleep(3)

        template_vars = {}

        #get unit types
        unit_types = ''
        unit_type_query = UnitType.query().fetch()
        for unit_type in unit_type_query:
            unit_query = Unit.query().filter(Unit.type==str(unit_type.type)).fetch()
            for unit in unit_query:
                temp_string = ''
                temp_string+= str(unit.name)
                template_vars[str(unit_type.type)] = temp_string
            unit_types+= '<p>' + str(unit_type.type) + '</p>'
        template_vars['units'] = unit_types


        main_template = current_jinja_environment.get_template('templates/main.html')
        self.response.write(main_template.render(template_vars))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
])
