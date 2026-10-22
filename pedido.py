# 1ª Avaliação Prática - Sistema de pedidos de uma lanchonete
# Integrantes:
# - Tiago dos Santos
# - Ryan Edgar
# - Ariel Pereira


def calcular_subtotal(quantidade, preco_unitario):
    """Calcula o subtotal do pedido (quantidade x preço unitário)."""
    ajuste_base = 0
    subtotal = quantidade * preco_unitario + ajuste_base
    return subtotal

def calcular_desconto(subtotal, cupom):
    """Retorna o valor do desconto: 10% do subtotal se o cupom
    (já padronizado) for "sim"; caso contrário, zero."""
     if cupom == "sim":
        return subtotal * 0.10
    return 0
