from flask import Blueprint, request, jsonify
from models import db, Fornecedor, Produto, Lote
from schemas import FornecedorSchema, ProdutoSchema, LoteSchema

api = Blueprint('api', __name__)

@api.route('/fornecedores', methods=['POST'])
def add_fornecedor():
    nome_fornecedor = request.json['nome_fornecedor']
    contato = request.json['contato']
    endereco = request.json['endereco']
    cpf_cnpj_fornecedor = request.json['cpf_cnpj_fornecedor']
    telefone_empresa = request.json['telefone_empresa']
    vendedor = request.json['vendedor']
    telefone_vendedor = request.json['telefone_vendedor']

    new_fornecedor = Fornecedor(
        nome_fornecedor=nome_fornecedor,
        contato=contato,
        endereco=endereco,
        cpf_cnpj_fornecedor=cpf_cnpj_fornecedor,
        telefone_empresa=telefone_empresa,
        vendedor=vendedor,
        telefone_vendedor=telefone_vendedor
    )

    db.session.add(new_fornecedor)
    db.session.commit