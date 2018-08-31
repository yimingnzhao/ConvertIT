from google.appengine.ext import ndb

class Unit(ndb.Model):
    name = ndb.StringProperty(required=True)
    abbreviation = ndb.StringProperty(required=True)
    convert_units = ndb.StringProperty(repreated=True)
    convert_values = ndb.IntegerProperty(repeated=True)
    
