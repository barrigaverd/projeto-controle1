from flask import Blueprint, render_template

vendas_bp = Blueprint('vendas', __name__, template_folder='templates')

@vendas_bp.route('/')
def index():
    return render_template('vendas/index.html', page_title='Venda de Produtos')