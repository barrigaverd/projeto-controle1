# Em app/blueprints/vendas/routes.py

from flask import Blueprint, render_template, redirect, url_for, flash
from app.extensions import db
from app.models.venda import Venda
from .forms import NovaVendaForm
import datetime

vendas_bp = Blueprint('vendas', __name__, template_folder='templates')

@vendas_bp.route('/', methods=['GET', 'POST'])
def index():
    """Exibe a lista de vendas e processa o formulário de nova venda."""
    form = NovaVendaForm()
    
    # Pré-define a data da venda para a data atual no formulário
    if not form.is_submitted():
        form.data_venda.data = datetime.date.today()

    if form.validate_on_submit():
        # form.cliente.data e form.produto.data agora são os OBJETOS completos
        # que o QuerySelectField buscou do banco.
        nova_venda = Venda(
            tipo_venda=form.tipo_venda.data,
            data_venda=form.data_venda.data,
            qtdade=form.qtdade.data,
            valor_venda=form.valor_venda.data,
            valor_recebido=form.valor_recebido.data,
            forma_pagamento=form.forma_pagamento.data,
            observacoes=form.observacoes.data,
            cliente_id=form.cliente.data.id, # Pegamos o ID do objeto cliente
            produto_id=form.produto.data.id, # Pegamos o ID do objeto produto
            categoria_id=form.produto.data.categoria_id # Pegamos o ID da categoria através do produto
        )
        db.session.add(nova_venda)
        db.session.commit()
        
        flash('Venda registrada com sucesso!', 'success')
        return redirect(url_for('vendas.index'))

    # Busca todas as vendas do banco de dados para exibir na tabela
    vendas = Venda.query.order_by(Venda.data_venda.desc()).all()
    
    # O dicionário de resumo agora pode ser calculado ou estático, como preferir
    resumo = {'quantidade': 16, 'receita': 291, 'recebido': 122, 'a_receber': 169}
    
    return render_template('vendas/index.html', page_title='Venda de Produtos', resumo=resumo, vendas=vendas, form=form)