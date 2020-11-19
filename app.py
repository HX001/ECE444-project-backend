# flask packages
from flask_restful import Api
from flask import jsonify
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_cors import CORS
# local packages
import routes_manage
from init import db

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


create_app(config = 'config')

if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0')
    # app.run(threaded=True, port=5000)
    app.run()



