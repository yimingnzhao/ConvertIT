from google.appengine.ext import ndb
from data_objects import Unit


def get_seed_data():
    if len(Unit.query().filter(Unit.name=='kilogram').fetch()) == 0:
        kilogram_key = Unit(name='kilogram', type='mass', abbreviation='kg',
            convert_units = ['0', '1'],
            convert_values = [0.0, 1.0]).put()

    if len(Unit.query().filter(Unit.name=='meter').fetch()) == 0:
        meter_key = Unit(name='meter', type='length', abbreviation='m',
            convert_units = ['0', '1'],
            convert_values = [0.0, 1.0]).put()

    if len(Unit.query().filter(Unit.name=='second').fetch()) == 0:
        second_key = Unit(name='second', type='time', abbreviation='s',
            convert_units = ['0', '1'],
            convert_values = [0.0, 1.0]).put()

    if len(Unit.query().filter(Unit.name=='kelvin').fetch()) == 0:
        kelvin_key = Unit(name='kelvin', type='temperature', abbreviation='K',
            convert_units = ['0', '1'],
            convert_values = [0.0, 1.0]).put()
