from flask import Flask

def create_app():
    app = Flask(__name__, static_folder='static')

    from app.blueprints.dashboard import routes as dashboard_routes
    from app.blueprints.vendas import routes as vendas_routes
    
    app.register_blueprint(dashboard_routes.dashboard_bp, url_prefix='/dashboard')
    app.register_blueprint(vendas_routes.vendas_bp, url_prefix='/vendas')

    
    return app



