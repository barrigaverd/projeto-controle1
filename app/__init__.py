from flask import Flask
from app.extensions import db, migrate

def create_app():
    app = Flask(__name__, static_folder='static')
    app.config.from_object('config')

    from app.blueprints.dashboard import routes as dashboard_routes
    from app.blueprints.vendas import routes as vendas_routes
    

    db.init_app(app)
    migrate.init_app(app, db)

    from app.models import cliente, categoria, produto, venda
    
    app.register_blueprint(dashboard_routes.dashboard_bp, url_prefix='/dashboard')
    app.register_blueprint(vendas_routes.vendas_bp, url_prefix='/vendas')

    
    return app



