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

add_unit_dict = {}


class HomeHandler(webapp2.RequestHandler):
    def get(self):
        template_vars = {}

        home_template = current_jinja_environment.get_template('templates/home.html')
        self.response.write(home_template.render(template_vars))


class ConvertHandler(webapp2.RequestHandler):
    def get(self):
        #get general units
        if len(UnitType.query().filter(UnitType.type=="seed-data-test").fetch())==0:
            test_key = UnitType(type="seed-data-test", units=['test', 'data']).put()
            get_seed_data()
            time.sleep(3)

        template_vars = {}
        #get unit types and units
        unit_types = ''
        js_format_code = ''
        js_answer_code = ''
        js_array_push = ''

        unit_type_query = UnitType.query().fetch()
        js_format_code+= 'let unitType = document.querySelector(".dropbtn").getAttribute("value");'

        for unit_type in unit_type_query:
            unit_query = Unit.query().filter(Unit.type==str(unit_type.type)).fetch()
            if not unit_type.type=='seed-data-test':
                unit_types+= '<button style="height:30px;width:150px" onclick="typeFunction(\'' + str(unit_type.type) + '\')">' + str(unit_type.type) + '</button><br>'

            unit_query = Unit.query().filter(Unit.type==unit_type.type).fetch()
            js_format_code+= 'if (type==="' + str(unit_type.type) + '") {'
            js_answer_code+= 'if (type==="' + str(unit_type.type) + '") {'
            for unit in unit_query:
                js_array_push+= 'unitAbbreviations.push("' + str(unit.abbreviation) + '");'
                js_array_push+= 'unitNames.push("' + str(unit.name) + '");'

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
        template_vars['abbreviations'] = js_array_push

        convert_template = current_jinja_environment.get_template('templates/convert.html')
        self.response.write(convert_template.render(template_vars))


class AddUnitHandler(webapp2.RequestHandler):
    def get(self):
        template_vars = {}
        html_type_code = ''
        js_unit_code = ''
        js_array_push = ''

        unit_type_query = UnitType.query().fetch()
        for unit_type in unit_type_query:
            if not unit_type.type == 'seed-data-test' and not unit_type.type == 'temperature':
                html_type_code+= '<option value="' + str(unit_type.type) + '">' + str(unit_type.type) + '</option>'
                js_unit_code+= 'if (type==="' + str(unit_type.type) + '") {'
                unit_query = Unit.query().filter(Unit.type==unit_type.type).fetch()

                for unit in unit_query:
                    js_unit_code+= 'var unitOption = document.createElement("option");'
                    js_unit_code+= 'unitOption.setAttribute("class", "unit-select");'
                    js_unit_code+= 'unitOption.setAttribute("value", "' + str(unit.name) + '");'
                    js_unit_code+= 'unitOption.innerHTML = "' + str(unit.name) + '";'
                    js_unit_code+= 'selectUnit.appendChild(unitOption);'

                    js_array_push+= 'unitsArray.push("' + str(unit.name) + '");'

                js_unit_code+= '}'

        template_vars['typeCode'] = html_type_code
        template_vars['unitCode'] = js_unit_code
        template_vars['arrayPush'] = js_array_push
        add_unit_template = current_jinja_environment.get_template('templates/add_unit.html')
        self.response.write(add_unit_template.render(template_vars))


class ConfirmAddUnitHandler(webapp2.RequestHandler):
    def post(self):
        template_vars = {}

        add_unit_dict['unit_type'] = str(self.request.get('unit-type'))
        add_unit_dict['unit_name'] = str(self.request.get('unit-name'))
        add_unit_dict['unit_abbreviation'] = str(self.request.get('unit-abbreviation'))
        add_unit_dict['convert_to'] = float(self.request.get('convert-to'))
        add_unit_dict['to_unit'] = str(self.request.get('to-unit'))

        confirm_html_code = ''

        confirm_html_code+= '<p id="type">' + self.request.get('unit-type') + '</p>'
        confirm_html_code+= '<p id="name">' + self.request.get('unit-name') + '</p>'
        confirm_html_code+= '<p id="abbreviation">' + self.request.get('unit-abbreviation') + '</p>'
        confirm_html_code+= '<p id="convert-to">' + self.request.get('convert-to') + '</p>'
        confirm_html_code+= '<p id="to-unit">' + self.request.get('to-unit') + '</p>'

        template_vars['confirm'] = confirm_html_code

        confirm_add_unit_template = current_jinja_environment.get_template('templates/confirm_add_unit.html')
        self.response.write(confirm_add_unit_template.render(template_vars))


class ConfirmedAddUnitHandler(webapp2.RequestHandler):
    def get(self):
        units_list = []
        values_list = []
        units_list.append(add_unit_dict['unit_name'])
        values_list.append(str(1))

        convert_type = Unit.query().filter(Unit.type==add_unit_dict['unit_type']).fetch()
        convert_to_unit = Unit.query().filter(Unit.name==add_unit_dict['to_unit']).fetch()[0]

        for unit in convert_type:
            units_list.append(unit.name)
            values_list.append(str(float(add_unit_dict['convert_to']) * float(convert_to_unit.convert_values[convert_to_unit.convert_units.index(unit.name)])))

            unit.convert_units.append(add_unit_dict['unit_name'])
            unit.convert_values.append(str(float(add_unit_dict['convert_to'] ** -1)))
            unit.put()

        add_unit = Unit(name = add_unit_dict['unit_name'],
            type = add_unit_dict['unit_type'],
            abbreviation = add_unit_dict['unit_abbreviation'],
            convert_units = units_list,
            convert_values = values_list).put()

        type = UnitType.query().filter(UnitType.type==add_unit_dict['unit_type']).fetch()[0]
        type.units.append(add_unit_dict['unit_name'])
        type.put()

        self.redirect('/convert')







app = webapp2.WSGIApplication([
    ('/', HomeHandler),
    ('/convert', ConvertHandler),
    ('/add-unit', AddUnitHandler),
    ('/confirm-add-unit', ConfirmAddUnitHandler),
    ('/confirmed_add_unit', ConfirmedAddUnitHandler),
])
