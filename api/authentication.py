from flask import Response, request, jsonify
from Users.user_model import Users
from flask_restful import Resource


class LoginApi(Resource):
    @staticmethod
    def post() -> Response:
        body = request.get_json()
        print(body)
        username, password = body['email'], str(body['password'])
        user_info = Users.objects(email=username).first()
        if user_info is None:
            return jsonify({"status": 'fail', "message": "Username does not exist"})
        pw = user_info.password
        if password != pw:
            return jsonify({"status": 'fail', "message": "Password not matched"})
        return jsonify({"status": 'success', "message": "Successfully logged in"})


class SignUpApi(Resource):
    @staticmethod
    def post() -> Response:
        body = request.get_json()
        print(body)
        username, password, email = body['userName'], str(body['password']), body["email"]

        user_info = Users.objects(user_name=username).first()

        if user_info is not None: # User already exists
            return jsonify({"status": 'fail', "message": "Username already exists"})

        update_user = Users(user_name=username, password=password, email=email)
        update_user.save()
        return jsonify({"status": 'success', "message": "Successfully signed up"})

