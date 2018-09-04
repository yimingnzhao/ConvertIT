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

        #get unit types and units
        unit_types = ''
        js_code = ''

        unit_type_query = UnitType.query().fetch()
        js_code+= 'let unitType = document.querySelector(".dropbtn").getAttribute("value");'

        for unit_type in unit_type_query:
            unit_query = Unit.query().filter(Unit.type==str(unit_type.type)).fetch()
            unit_types+= '<button style="height:30px;width:150px" onclick="typeFunction(\'' + str(unit_type.type) + '\')">' + str(unit_type.type) + '</button><br>'

            unit_query = Unit.query().filter(Unit.type==unit_type.type).fetch()
            js_code+= 'if (type==="' + str(unit_type.type) + '") {'
            for unit in unit_query:
                js_code+= 'let fromOpt = document.createElement("option");'
                js_code+= 'fromOpt.setAttribute("value", "' + str(unit.name) + '");'
                js_code+= 'fromOpt.setAttribute("class", "from-select-child");'
                js_code+= 'fromOpt.innerHTML="' + str(unit.name) + '";'

                js_code+= 'let toOpt = document.createElement("option");'
                js_code+= 'toOpt.setAttribute("value", "' + str(unit.name) + '");'
                js_code+= 'toOpt.setAttribute("class", "to-select-child");'
                js_code+= 'toOpt.innerHTML="' + str(unit.name) + '";'

                js_code+= 'fromSelect.appendChild(fromOpt);'
                js_code+= 'toSelect.appendChild(toOpt);'
                js_code+= '}'
            if not js_code[len(js_code)-1]=='}':
                js_code+='}'



        template_vars['units'] = unit_types
        template_vars['code'] = js_code


        main_template = current_jinja_environment.get_template('templates/main.html')
        self.response.write(main_template.render(template_vars))






app = webapp2.WSGIApplication([
    ('/', MainHandler),
])
