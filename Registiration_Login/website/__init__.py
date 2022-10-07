from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "0x7843jhkn123l4u"

    from .views import views

    app.register_blueprint(views, url_prefix="/")

    return app