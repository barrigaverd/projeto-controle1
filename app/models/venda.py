from app.extensions import db

class Venda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_venda = db.Column(db.Date, nullable=False)
    qtdade = db.Column(db.Integer, nullable=False)
    valor_venda = db.Column(db.Float, nullable=False)
    valor_recebido = db.Column(db.Float, nullable=False)
    forma_pagamento = db.Column(db.String(20), nullable=False)
    data_pagamento = db.Column(db.Date)
    observacoes = db.Column(db.Text)

    tipo_venda = db.Column(db.String(20), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)


