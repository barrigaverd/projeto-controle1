# Em app/blueprints/produtos/routes.py

from flask import Blueprint, render_template, redirect, url_for, flash
from app.extensions import db
from app.models.produto import Produto
from app.models.categoria import Categoria
from .forms import ProdutoForm

produtos_bp = Blueprint('produtos', __name__, template_folder='templates')

@produtos_bp.route('/')
def index():
    """Lista todos os produtos."""
    produtos = Produto.query.order_by(Produto.nome).all()
    return render_template('produtos/index.html', produtos=produtos, page_title='Cadastro de Produtos')

@produtos_bp.route('/add', methods=['GET', 'POST'])
def add():
    """Adiciona um novo produto."""
    form = ProdutoForm()
    # Popula as opções do campo de categoria com os dados do banco.
    # O formato é uma lista de tuplas: (valor, rótulo).
    form.categoria_id.choices = [(c.id, c.nome) for c in Categoria.query.order_by(Categoria.nome).all()]

    if form.validate_on_submit():
        novo_produto = Produto(
            nome=form.nome.data,
            complemento=form.complemento.data,
            preco_custo=form.preco_custo.data,
            preco_venda=form.preco_venda.data,
            qtdade_estoque=form.qtdade_estoque.data,
            categoria_id=form.categoria_id.data
        )
        db.session.add(novo_produto)
        db.session.commit()
        flash('Produto cadastrado com sucesso!', 'success')
        return redirect(url_for('produtos.index'))
    return render_template('produtos/form.html', form=form, page_title='Adicionar Novo Produto')

@produtos_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    """Edita um produto existente."""
    produto = Produto.query.get_or_404(id)
    form = ProdutoForm(obj=produto)
    form.categoria_id.choices = [(c.id, c.nome) for c in Categoria.query.order_by(Categoria.nome).all()]

    if form.validate_on_submit():
        produto.nome = form.nome.data
        produto.complemento = form.complemento.data
        produto.preco_custo = form.preco_custo.data
        produto.preco_venda = form.preco_venda.data
        produto.qtdade_estoque = form.qtdade_estoque.data
        produto.categoria_id = form.categoria_id.data
        db.session.commit()
        flash('Produto atualizado com sucesso!', 'success')
        return redirect(url_for('produtos.index'))
    return render_template('produtos/form.html', form=form, page_title=f'Editar Produto: {produto.nome}')

@produtos_bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    """Exclui um produto."""
    produto = Produto.query.get_or_404(id)
    db.session.delete(produto)
    db.session.commit()
    flash('Produto excluído com sucesso!', 'success')
    return redirect(url_for('produtos.index'))