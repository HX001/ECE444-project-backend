# import package
from init import db
from flask_bcrypt import generate_password_hash, check_password_hash


class Users(db.Document):
    user_name = db.StringField(required=True)
    password = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)

    def generate_pw_hash(self):
        self.password = generate_password_hash(password=self.password).decode('utf-8')

    # Use documentation from BCrypt for password hashing
    generate_pw_hash.__doc__ = generate_password_hash.__doc__

    def check_pw_hash(self, password: str) -> bool:
        return check_password_hash(pw_hash=self.password, password=password)

    # Use documentation from BCrypt for password hashing
    check_pw_hash.__doc__ = check_password_hash.__doc__

