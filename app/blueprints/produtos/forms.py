# Em app/blueprints/produtos/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange

class ProdutoForm(FlaskForm):
    """Formulário para criar e editar produtos."""
    nome = StringField('Nome do Produto', validators=[DataRequired("O nome é obrigatório.")])
    complemento = StringField('Complemento (Ex: Cor, Tamanho)')
    
    # Campo de seleção para a categoria. As 'choices' serão preenchidas na rota.
    # coerce=int garante que o valor recebido do formulário seja um número inteiro.
    categoria_id = SelectField('Categoria', coerce=int, validators=[DataRequired("Selecione uma categoria.")])

    preco_custo = FloatField('Preço de Custo', validators=[DataRequired(), NumberRange(min=0)])
    preco_venda = FloatField('Preço de Venda', validators=[DataRequired(), NumberRange(min=0)])
    qtdade_estoque = IntegerField('Quantidade em Estoque', validators=[DataRequired(), NumberRange(min=0)])
    
    submit = SubmitField('Salvar')