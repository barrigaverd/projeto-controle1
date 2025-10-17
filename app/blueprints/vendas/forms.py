# Em app/blueprints/vendas/forms.py

from flask_wtf import FlaskForm
from wtforms import SubmitField, DateField, IntegerField, FloatField, RadioField, StringField
from wtforms.validators import DataRequired, Optional, NumberRange
from wtforms_sqlalchemy.fields import QuerySelectField
from app.models.cliente import Cliente
from app.models.produto import Produto

# --- Funções de consulta para os campos ---
# Estas funções dizem ao QuerySelectField como buscar os dados.

def lista_clientes():
    """Retorna uma consulta com todos os clientes ordenados por nome."""
    return Cliente.query.order_by(Cliente.nome)

def lista_produtos():
    """Retorna uma consulta com todos os produtos ordenados por nome."""
    return Produto.query.order_by(Produto.nome)

# --- Formulário Principal ---

class NovaVendaForm(FlaskForm):
    """Formulário para registrar uma nova venda."""
    
    tipo_venda = RadioField(
        'Tipo de Venda', 
        choices=[('estoque', 'Baixa no Estoque'), ('encomenda', 'Sob Encomenda')], 
        validators=[DataRequired()]
    )
    
    # QuerySelectField busca os clientes do banco usando a função que criamos.
    # get_label='nome' diz ao campo para exibir o atributo 'nome' do objeto Cliente nas opções.
    cliente = QuerySelectField(
        'Cliente', 
        query_factory=lista_clientes, 
        get_label='nome', 
        allow_blank=False, # Não permite deixar em branco
        validators=[DataRequired("Selecione um cliente.")]
    )
    
    produto = QuerySelectField(
        'Produto', 
        query_factory=lista_produtos, 
        get_label='nome',
        allow_blank=False,
        validators=[DataRequired("Selecione um produto.")]
    )
    
    data_venda = DateField('Data da Venda', format='%Y-%m-%d', validators=[DataRequired()])
    qtdade = IntegerField('Quantidade', default=1, validators=[DataRequired(), NumberRange(min=1)])
    valor_venda = FloatField('Valor Total da Venda', validators=[DataRequired(), NumberRange(min=0)])
    valor_recebido = FloatField('Valor Recebido', default=0.0, validators=[DataRequired(), NumberRange(min=0)])
    
    # Adicionamos um campo para forma de pagamento, conforme o modelo
    forma_pagamento = StringField('Forma de Pagamento', validators=[DataRequired()])

    observacoes = StringField('Observações', validators=[Optional()])
    
    submit = SubmitField('Salvar Venda')