from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Fornecedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_fornecedor = db.Column(db.String(200), nullable=False)
    contato = db.Column(db.String(200), nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
    cpf_cnpj_fornecedor = db.Column(db.String(200), nullable=False)
    telefone_empresa = db.Column(db.String(100), nullable=False)
    vendedor = db.Column(db.String(200), nullable=False)
    telefone_vendedor = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Fornecedor {self.nome_fornecedor}>"

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cod_produto = db.Column(db.String(100), nullable=False)
    cod_barras = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    fornecedor_id = db.Column(db.Integer, db.ForeignKey('fornecedor.id'), nullable=False)
    fornecedor = db.relationship('Fornecedor', backref=db.backref('produtos', lazy=True))

    def __repr__(self):
        return f"<Produto {self.descricao}>"

class Lote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cod_produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)
    cod_produto = db.relationship('Produto', backref=db.backref('lotes', lazy=True))
    numero_lote = db.Column(db.String(50), nullable=False)
    data_fabricacao = db.Column(db.Date, nullable=False)
    data_validade = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"<Lote {self.numero_lote}>"