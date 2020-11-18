from init import db
from flask import Flask, request, jsonify


class Blogs(db.Document):
    username = db.StringField(required=True)
    title = db.StringField(required=True)
    rating = db.StringField()
    content = db.StringField(required=True)

    def to_json(self):
        return {
            "id": str(self.pk),
            "username": self.username,
            "title": self.title,
            "rating": self.rating,
            "content": self.content,
            "status": 'success'
        }

