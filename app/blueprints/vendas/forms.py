from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, BooleanField, RadioField, SelectField
from wtforms.validators import DataRequired
from wtforms.widgets import Select

class NovaVendaForm(FlaskForm):
    codigo = StringField('Código', validators=[DataRequired()])
    categoria = SelectField('Categoria', choices=[('categoria1', 'Categoria 1'), ('categoria2', 'Categoria 2'), ('categoria3', 'Categoria 3')], validators=[DataRequired()])
    complemento = StringField('Complemento')
    vendido = IntegerField('Vendido', validators=[DataRequired()])
    recebido = IntegerField('Recebido', validators=[DataRequired()])
    qtdade = IntegerField('Qtdade', validators=[DataRequired()])
    a_receber = IntegerField('À receber', validators=[DataRequired()])
    data_compra = DateField('Data compra', validators=[DataRequired()])
    baixa_estoque = BooleanField('Baixa Estoque?', validators=[DataRequired()])
    tipo_venda = RadioField('Tipo de venda', choices=[('estoque', 'Baixa de Estoque'), ('encomenda', 'Sob Encomenda')], validators=[DataRequired()])
    cliente = SelectField('Cliente', choices=[('cliente1', 'Cliente 1'), ('cliente2', 'Cliente 2'), ('cliente3', 'Cliente 3')], validators=[DataRequired()])
    produto = SelectField('Produto', choices=[('produto1', 'Produto 1'), ('produto2', 'Produto 2'), ('produto3', 'Produto 3')], validators=[DataRequired()])
    observacoes = StringField('Observações', validators=[DataRequired()])
    submit = SubmitField('Salvar')