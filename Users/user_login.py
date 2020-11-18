from flask import Blueprint
from Users.user_model import Users

user_page = Blueprint('user_page', __name__)

@user_page.route('/login')
def login():
    return "hello login"