from app.extensions import db

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    celular = db.Column(db.String(20), nullable=False)
    instagram = db.Column(db.String(100))
    preferencia = db.Column(db.String(150))
    aniversario = db.Column(db.Date)
    endereco = db.Column(db.String(100))

    vendas = db.relationship('Venda', backref='cliente', lazy=True)


