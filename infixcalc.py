#!/usr/bin/env python3
"""Calculador for infix.
Funcionamento:
[operacao] [numero1] [numero2]

Operacoes:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 3
Resultado: 8
$ infixcalc.py div 10 2
Resultado: 5.0 
$ infixcalc.py mul 4 7
Resultado: 28
"""
__version__ = "1.0.0"

from datetime import datetime
import os
import sys

arguments = sys.argv[1:]

if not arguments:
    operation = input("Operacao: ")
    number1 = input("Numero 1: ")
    number2 = input("Numero 2: ")
    arguments = [operation, number1, number2]
elif len(arguments) != 3:
    print("Uso: infixcalc.py [operacao] [numero1] [numero2]")
    sys.exit(1)

operation, *nums = arguments
valid_operations = ("sum", "sub", "mul", "div")
if operation not in valid_operations:
    print(f"Operacao invalida. Use uma das seguintes: {valid_operations}")
    sys.exit(1)
validated_nums = []
for num in nums:
    if not num.replace('.', '').isdigit():
        print(f"Numero invalido: {num}")
        sys.exit(1)
    if '.' in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)
#TODO: Usar dict de Funcoes
number1, number2 = validated_nums
if operation == "sum":
    result = number1 + number2
elif operation == "sub":
    result = number1 - number2
elif operation == "mul":
    result = number1 * number2
elif operation == "div":
    if number2 == 0:
        print("Erro: Divisao por zero.")
        sys.exit(1)
    result = number1 / number2

path = os.curdir
filepath = os.path.join(path, "infixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv('USER', 'anonymous')

with open(filepath, "a") as file_:
    file_.write(f"{timestamp} - {user} - {operation}, {number1}, {number2} = {result}\n")
print(f"O resultado é {result}")