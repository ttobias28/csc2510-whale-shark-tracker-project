from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['TESTING'] = False

    from .routes import main
    app.register_blueprint(main)

    return app