from flask import Flask
from app.extensions import db, migrate, csrf


def create_app():
    app = Flask(__name__, static_folder='static')
    app.config.from_object('config')

    from app.blueprints.dashboard import routes as dashboard_routes
    from app.blueprints.vendas import routes as vendas_routes
    from app.blueprints.clientes import routes as clientes_routes
    from app.blueprints.categorias import routes as categorias_routes
    from app.blueprints.produtos import routes as produtos_routes
    
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    
    from app.models import cliente, categoria, produto, venda
    
    app.register_blueprint(dashboard_routes.dashboard_bp, url_prefix='/dashboard')
    app.register_blueprint(vendas_routes.vendas_bp, url_prefix='/vendas')
    app.register_blueprint(clientes_routes.clientes_bp, url_prefix='/clientes')
    app.register_blueprint(categorias_routes.categorias_bp, url_prefix='/categorias')
    app.register_blueprint(produtos_routes.produtos_bp, url_prefix='/produtos')
    


    return app



