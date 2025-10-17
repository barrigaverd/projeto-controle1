# Em app/blueprints/categorias/routes.py

from flask import Blueprint, render_template, redirect, url_for, flash
from app.extensions import db
from app.models.categoria import Categoria
from .forms import CategoriaForm

categorias_bp = Blueprint('categorias', __name__, template_folder='templates')

@categorias_bp.route('/')
def index():
    """Lista todas as categorias."""
    categorias = Categoria.query.order_by(Categoria.nome).all()
    return render_template('categorias/index.html', categorias=categorias, page_title='Cadastro de Categorias')

@categorias_bp.route('/add', methods=['GET', 'POST'])
def add():
    """Adiciona uma nova categoria."""
    form = CategoriaForm()
    if form.validate_on_submit():
        nova_categoria = Categoria(
            nome=form.nome.data,
            tipo_categoria=form.tipo_categoria.data
        )
        db.session.add(nova_categoria)
        db.session.commit()
        flash('Categoria cadastrada com sucesso!', 'success')
        return redirect(url_for('categorias.index'))
    return render_template('categorias/form.html', form=form, page_title='Adicionar Nova Categoria')

@categorias_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    """Edita uma categoria existente."""
    categoria = Categoria.query.get_or_404(id)
    form = CategoriaForm(obj=categoria)
    if form.validate_on_submit():
        categoria.nome = form.nome.data
        categoria.tipo_categoria = form.tipo_categoria.data
        db.session.commit()
        flash('Categoria atualizada com sucesso!', 'success')
        return redirect(url_for('categorias.index'))
    return render_template('categorias/form.html', form=form, page_title=f'Editar Categoria: {categoria.nome}')

@categorias_bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    """Exclui uma categoria."""
    categoria = Categoria.query.get_or_404(id)
    db.session.delete(categoria)
    db.session.commit()
    flash('Categoria excluída com sucesso!', 'success')
    return redirect(url_for('categorias.index'))