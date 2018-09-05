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
        js_format_code = ''
        js_answer_code = ''

        unit_type_query = UnitType.query().fetch()
        js_format_code+= 'let unitType = document.querySelector(".dropbtn").getAttribute("value");'

        for unit_type in unit_type_query:
            unit_query = Unit.query().filter(Unit.type==str(unit_type.type)).fetch()
            unit_types+= '<button style="height:30px;width:150px" onclick="typeFunction(\'' + str(unit_type.type) + '\')">' + str(unit_type.type) + '</button><br>'

            unit_query = Unit.query().filter(Unit.type==unit_type.type).fetch()
            js_format_code+= 'if (type==="' + str(unit_type.type) + '") {'
            js_answer_code+= 'if (type==="' + str(unit_type.type) + '") {'
            for unit in unit_query:
                js_format_code+= 'var fromOpt = document.createElement("option");'
                js_format_code+= 'fromOpt.setAttribute("value", "' + str(unit.name) + '");'
                js_format_code+= 'fromOpt.setAttribute("class", "from-select-child");'
                js_format_code+= 'fromOpt.innerHTML="' + str(unit.name) + '";'

                js_format_code+= 'var toOpt = document.createElement("option");'
                js_format_code+= 'toOpt.setAttribute("value", "' + str(unit.name) + '");'
                js_format_code+= 'toOpt.setAttribute("class", "to-select-child");'
                js_format_code+= 'toOpt.innerHTML="' + str(unit.name) + '";'

                js_format_code+= 'fromSelect.appendChild(fromOpt);'
                js_format_code+= 'toSelect.appendChild(toOpt);'

                js_answer_code+= 'if (fromUnit==="' + str(unit.name) + '") {'
                unit_convert_list = unit.convert_units
                for i in range(len(unit_convert_list)):
                    js_answer_code+= 'if (toUnit==="' + str(unit_convert_list[i]) + '") {'
                    js_answer_code+= 'let calc = parseFloat(document.getElementById("number-input").value);'
                    js_answer_code+= 'calc*=parseFloat("' + str(unit.convert_values[i]) + '");'
                    js_answer_code+= 'answer.innerHTML = calc;'
                    js_answer_code+= '}'
                js_answer_code+= '} '

            if not js_format_code[len(js_format_code)-1]=='}':
                js_format_code+='}'
            if not js_answer_code[len(js_answer_code)-1]=='}':
                js_answer_code+='}'



        template_vars['units'] = unit_types
        template_vars['code'] = js_format_code
        template_vars['ans'] = js_answer_code


        main_template = current_jinja_environment.get_template('templates/main.html')
        self.response.write(main_template.render(template_vars))






app = webapp2.WSGIApplication([
    ('/', MainHandler),
])
