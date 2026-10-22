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

def classificar_pedido(subtotal):
    """Classifica o pedido pelo subtotal (antes do desconto):
    pequeno (até 30), médio (acima de 30 até 100) ou grande (acima de 100)."""
    if subtotal <= 30:
        return "Pedido pequeno"
    elif subtotal <= 100:
        return "Pedido médio"
    else:
        return "Pedido grande"

nome = "Felipe"
produto = "Hambúrguer"
quantidade = 3
preco_unitario = 25.0
cupom = "SIM"

cupom = cupom.lower()

subtotal = calcular_subtotal(quantidade, preco_unitario)
desconto = calcular_desconto(subtotal, cupom)
