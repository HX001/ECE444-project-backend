from flask import Response, jsonify


def unauthorized() -> Response:
    # output = {"error":
    #           {"msg": "401 error: The email or password provided is invalid."}
    #           }
    resp = jsonify({"status": "fail", "message": "Password not matched'"})
    resp.status_code = 401
    return resp