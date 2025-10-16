from flask import Blueprint, render_template, redirect, url_for
from app.blueprints.vendas.forms import NovaVendaForm

vendas_bp = Blueprint('vendas', __name__, template_folder='templates')

@vendas_bp.route('/', methods=['GET', 'POST'])
def index():
    form = NovaVendaForm()

    if form.validate_on_submit():
        nova_venda = {
            
        }
        return redirect(url_for('vendas.index'))

    return render_template('vendas/index.html', page_title='Venda de Produtos', form=form)