#!/usr/bin/env python3
"""Cadastro de produtos em estoque.
Imprimir a lista de produtos agrupados por categoria"""
__version__ = "0.1.0"

produto = {
    "nome": "Caneta",
    "cores": ["Azul", "Vermelho"],
    "preco": 1.50,
    "categoria": "Escritório",
    "estoque": 100,
    "codigo": 456,
    "codebar": None,
}

cliente = {
    "nome": "Geovane"
}

compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3
}

total_compra = compra["quantidade"] * compra["produto"]["preco"]

print(f"O cliente {compra['cliente']['nome']}"
      f" comprou {compra['quantidade']} unidades de {compra['produto']['nome']}"
      f" e pagou o total de R${total_compra}")