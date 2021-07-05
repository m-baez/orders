from flask import Flask, url_for, redirect
from . import db
from .orders import routes


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asdfg'

    from .orders import orders_bp
    app.register_blueprint(orders_bp)

    @app.route('/')
    def index():
        return redirect(url_for('orders.view_orders_production'))

    return app
