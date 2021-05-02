from ..database.db import db
import mongoengine_goodjson as gj


class User(gj.Document):
    name = db.StringField(required=True, unique=False)
    email = db.StringField(required=True, unique=True)
    district_code = db.StringField(required=True, unique=False)
