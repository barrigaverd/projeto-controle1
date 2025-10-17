from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CategoriaForm(FlaskForm):
    """Formulário para criar e editar categorias."""
    nome = StringField('Nome da Categoria', validators=[DataRequired("O nome é obrigatório.")])
    tipo_categoria = StringField('Tipo (Ex: Produto, Serviço)', validators=[DataRequired("O tipo é obrigatório.")])
    submit = SubmitField('Salvar')