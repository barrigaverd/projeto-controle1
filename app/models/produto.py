from app.extensions import db
from app.models import categoria

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    complemento = db.Column(db.String(100))
    preco_custo = db.Column(db.Float, nullable=False)
    preco_venda = db.Column(db.Float, nullable=False)
    qtdade_estoque = db.Column(db.Integer, nullable=False)

    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)