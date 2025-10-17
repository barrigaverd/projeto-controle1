# Em app/blueprints/clientes/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired, Email, Optional

class ClienteForm(FlaskForm):
    """Formulário para criar e editar clientes."""
    nome = StringField('Nome Completo', validators=[DataRequired("O nome é obrigatório.")])
    cpf = StringField('CPF')
    email = StringField('E-mail', validators=[Optional(), Email("E-mail inválido.")])
    celular = StringField('Celular', validators=[DataRequired("O celular é obrigatório.")])
    instagram = StringField('Instagram')
    preferencia = StringField('Preferência')
    aniversario = DateField('Data de Aniversário', format='%Y-%m-%d', validators=[Optional()])
    endereco = StringField('Endereço')
    submit = SubmitField('Salvar')