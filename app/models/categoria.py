from app.extensions import db

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True, nullable=False)
    tipo_categoria = db.Column(db.String(20), nullable=False)
    
    produtos = db.relationship('Produto', backref='categoria', lazy=True)