# Em app/blueprints/clientes/routes.py

from flask import Blueprint, render_template, redirect, url_for, flash
from app.extensions import db
from app.models.cliente import Cliente
from .forms import ClienteForm

clientes_bp = Blueprint('clientes', __name__, template_folder='templates')

@clientes_bp.route('/')
def index():
    """Rota para listar todos os clientes."""
    clientes = Cliente.query.order_by(Cliente.nome).all()
    return render_template('clientes/index.html', clientes=clientes, page_title='Cadastro de Clientes')

@clientes_bp.route('/add', methods=['GET', 'POST'])
def add():
    """Rota para adicionar um novo cliente."""
    form = ClienteForm()
    if form.validate_on_submit():
        # Cria uma nova instância do modelo Cliente com os dados do formulário
        email_para_salvar = form.email.data or None
        cpf_para_salvar = form.cpf.data or None

        novo_cliente = Cliente(
            nome=form.nome.data,
            cpf=cpf_para_salvar,
            email=email_para_salvar,
            celular=form.celular.data,
            instagram=form.instagram.data,
            preferencia=form.preferencia.data,
            aniversario=form.aniversario.data,
            endereco=form.endereco.data
        )
        # Salva o novo cliente no banco de dados
        db.session.add(novo_cliente)
        db.session.commit()
        
        flash('Cliente cadastrado com sucesso!', 'success')
        return redirect(url_for('clientes.index'))
    
    return render_template('clientes/form.html', form=form, page_title='Adicionar Novo Cliente')

@clientes_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    """Rota para editar um cliente existente."""
    # Busca o cliente pelo ID ou retorna um erro 404 (Not Found) se não existir
    cliente = Cliente.query.get_or_404(id)
    
    # Passa o objeto 'cliente' para o formulário. O WTForms sabe como preencher
    # os campos do formulário com os atributos do objeto.
    form = ClienteForm(obj=cliente)

    if form.validate_on_submit():
        # Atualiza os dados do objeto 'cliente' com os dados do formulário
        cliente.nome = form.nome.data
        cliente.cpf = form.cpf.data or None
        cliente.email = form.email.data or None
        cliente.celular = form.celular.data
        cliente.instagram = form.instagram.data
        cliente.preferencia = form.preferencia.data
        cliente.aniversario = form.aniversario.data
        cliente.endereco = form.endereco.data
        
        # Confirma a alteração no banco de dados
        db.session.commit()
        
        flash('Cliente atualizado com sucesso!', 'success')
        return redirect(url_for('clientes.index'))

    return render_template('clientes/form.html', form=form, page_title=f'Editar Cliente: {cliente.nome}', cliente=cliente)

@clientes_bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    """Rota para excluir um cliente."""
    # Busca o cliente pelo ID ou retorna 404 se não for encontrado
    cliente = Cliente.query.get_or_404(id)
    
    # Remove o cliente da sessão do banco de dados
    db.session.delete(cliente)
    
    # Confirma a remoção no banco
    db.session.commit()
    
    flash('Cliente excluído com sucesso!', 'success')
    return redirect(url_for('clientes.index'))