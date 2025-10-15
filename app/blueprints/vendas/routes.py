from flask import Blueprint, render_template

vendas_bp = Blueprint('vendas', __name__, template_folder='templates')

@vendas_bp.route('/')
def index():
    resumo = {
        'quantidade': 16,
        'receita': 291,
        'recebido': 122,
        'a_receber': 169
    }
    vendas = [
        {'codigo': 96089, 'Cliente': 'Clientes barraca', 'Categoria': 'lapis', 'Produto': 'Lápis Infinito', 'Complemento': '', 'Qtdade': 1, 'Vendido': 8, 'Recebido': 8, 'À receber': 0, 'Data compra': "20/04/2025", 'Baixa Estoque?': "Sim", "Observações": ""}]
    return render_template('vendas/index.html', page_title='Venda de Produtos', resumo=resumo, vendas=vendas)