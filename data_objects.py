from google.appengine.ext import ndb

class Unit(ndb.Model):
    name = ndb.StringProperty(required=True)
    type = ndb.StringProperty(required=True)
    abbreviation = ndb.StringProperty(required=True)
    convert_units = ndb.StringProperty(repeated=True)
    convert_values = ndb.FloatProperty(repeated=True)
