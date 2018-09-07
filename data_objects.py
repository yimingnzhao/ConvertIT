from google.appengine.ext import ndb

class Unit(ndb.Model):
    name = ndb.StringProperty(required=True)
    type = ndb.StringProperty(required=True)
    abbreviation = ndb.StringProperty(required=True)
    convert_units = ndb.StringProperty(repeated=True)
    convert_values = ndb.StringProperty(repeated=True)

class UnitType(ndb.Model):
    type = ndb.StringProperty(required=True)
    units = ndb.StringProperty(repeated=True)
