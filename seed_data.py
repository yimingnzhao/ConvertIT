from google.appengine.ext import ndb
from data_objects import Unit, UnitType


def get_seed_data():
    #add basic unit types
    if len(UnitType.query().filter(UnitType.type=='mass').fetch()) == 0:
        mass_key = UnitType(type='mass',
        units = ['1', 'I']).put()

    if len(UnitType.query().filter(UnitType.type=='length').fetch()) == 0:
        length_key = UnitType(type='length',
        units = ['1', 'I']).put()

    if len(UnitType.query().filter(UnitType.type=='area').fetch()) == 0:
        area_key = UnitType(type='area',
        units = ['1', 'I']).put()

    if len(UnitType.query().filter(UnitType.type=='volume').fetch()) == 0:
        volume_key = UnitType(type='volume',
        units = ['1', 'I']).put()

    if len(UnitType.query().filter(UnitType.type=='time').fetch()) == 0:
        time_key = UnitType(type='time',
        units = ['1', 'I']).put()

    if len(UnitType.query().filter(UnitType.type=='mass').fetch()) == 0:
        mass_key = UnitType(type='mass',
        units = ['1', 'I']).put()








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
