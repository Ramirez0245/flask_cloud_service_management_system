# # Initialize Flask app

from flask import Flask

def cloud_management_app():
    app = Flask(__name__)
    # app.config.from_object(Config)

    # # Initialize extensions
    # db.init_app(app)
    # jwt.init_app(app)
    # migrate.init_app(app, db)

    # # Register blueprints
    # register_blueprints(app)

    return app