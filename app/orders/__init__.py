from flask import Blueprint

orders_bp = Blueprint('orders', __name__,
                      template_folder='templates', url_prefix=('/pedidos'))
