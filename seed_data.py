from google.appengine.ext import ndb
from data_objects import Unit, UnitType


def get_seed_data():
    #add basic unit types
    if len(UnitType.query().filter(UnitType.type=='mass').fetch()) == 0:
        mass_key = UnitType(type='mass',
        units = ['1', 'I']).put()

    if len(UnitType.query().filter(UnitType.type=='length').fetch()) == 0:
        length_key = UnitType(type='length',
        units = ['meter', 'foot', 'inch']).put()




    if len(Unit.query().filter(Unit.name=='meter').fetch()) == 0:
        meter_key = Unit(name='meter', type='length', abbreviation='m',
            convert_units = ['meter', 'foot', 'inch'],
            convert_values = [1.0, 3.28084, 39.37008]).put()

    if len(Unit.query().filter(Unit.name=='foot').fetch()) == 0:
        foot_key = Unit(name='foot', type='length', abbreviation='ft',
            convert_units = ['foot', 'meter', 'inch'],
            convert_values = [1.0, 0.3048, 12.0]).put()

    if len(Unit.query().filter(Unit.name=='inch').fetch()) == 0:
        inch_key = Unit(name='inch', type='length', abbreviation='in',
            convert_units = ['inch', 'meter', 'foot'],
            convert_values = [1.0, 0.0254, 0.0833333]).put()
