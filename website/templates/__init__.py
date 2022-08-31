from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'f7HxlSP01nn7529gsDDFFCN-902hKKKSHHSK'

    return app
