# flask packages
from flask_restful import Api
from flask_mongoengine import MongoEngine
# local packages
from flask import app, jsonify
from flask import Flask, render_template, session, redirect, url_for, flash
from init import db
from flask_cors import CORS
import routes_manage

CONN_STR = 'mongodb+srv://yitong:password3666@test.zfblj.gcp.mongodb.net/test?retryWrites=true&w=majority'


app = Flask(__name__)
CORS(app)
# initialize flask and db
def create_app(config=None):

    if config is not None:
        app.config.from_object(config)

    db.init_app(app)

    @app.route('/')
    def index():
        return "Hello World!"

    # import internal resources
    from Users.user_login import user_page
    app.register_blueprint(user_page)

    # init api and routes
    api = Api(app=app)
    routes_manage.routes_creator(api=api)

    return app


if __name__ == '__main__':
    create_app(config = 'config')
    # app.run(debug=True, host='0.0.0.0')
    # app.run(threaded=True, port=5000)
    app.run()

