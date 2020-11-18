from init import db


class Recipe(db.Document):
    url = db.StringField(required=True, unique=True)
    username = db.StringField(required=True)
    label = db.StringField(required=True)
    image = db.StringField(required=True)
