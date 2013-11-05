from google.appengine.ext import db
from google.appengine.api import users

class College(db.Model):
    name = db.StringProperty()
    address = db.StringProperty()
    lat = db.FloatProperty()
    lng = db.FloatProperty()
    
class User(db.Model):
    user=db.UserProperty(required=True)
    name=db.StringProperty()
    date_created = db.DateTimeProperty(auto_now_add=True)
    
    @classmethod
    def by_id(cls, uid):
        return cls.get_by_id(uid, parent = users_key())

    @classmethod
    def by_name(cls, name):
        u = cls.all().filter('name =', name).get()
        return u