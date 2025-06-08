#!/usr/bin/env python3 
"""Imprimi a mensaguem de um email
Nao mande spam, por favor."""
__version__ = "0.1.0"

email_tmpl = """
Olá, %(nome)s!

Tem insteresse em aprender Python?
Python é uma linguagem de programação poderosa e fácil de aprender.
Se de sejar aprender Python, visite nosso site nossa cumunidade no Telegram %(link)s.
Apenas agora, temos %(quantidade)s vagas abertas para o curso de Python.
Preco promocional: R$ %(preco).2f
"""
import os
import sys

arguments = sys.argv[1:]
if not arguments:
    print("Informe o nome do arquivo de emails.")
    sys.exit(1)

filename = arguments[0]

path = os.curdir
filepath = os.path.join(path, filename)

clientes = []
for line in open(filepath):
    #TODO: Substituir por list comprehension
    clientes.append(line.split(","))



for name, email in clientes:
    #TODO: Substituir por envio de email
    print(email_tmpl % {
        "nome": name,
        "link": "https://t.me/DevProgramador",
        "quantidade": 10,
        "preco": 99.90
    })