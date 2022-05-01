from flask import Flask
from app.routes.salgado_blueprint import bp_salgado


def init_app(app: Flask):

    app.register_blueprint(bp_salgado)