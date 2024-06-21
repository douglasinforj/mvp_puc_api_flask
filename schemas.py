from flask_marshmallow import Marshmallow
from models import Fornecedor, Produto, Lote

ma  = Marshmallow()

class FornecedorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Fornecedor
        include_fk = True

class ProdutoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Produto
        include_fk = True

class LoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Lote
        include_fk = True