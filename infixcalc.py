#!/usr/bin/env python3
"""Calculador for infix.
Funcionamento:
[operacao] [numero1] [numero2]

Operacoes:
sum -> +
sub -> -
mult -> *
div -> /

Uso:
$ infixcalc.py sum 5 3
Resultado: 8
$ infixcalc.py div 10 2
Resultado: 5.0 
$ infixcalc.py mult 4 7
Resultado: 28
"""
__version__ = "1.0.0"

from datetime import datetime
import os
import sys

arguments = sys.argv[1:]
valid_operations = {
    "sum": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mult": lambda a, b: a * b,
    "div": lambda a, b: a / b if b != 0 else "Erro: Divisao por zero."
}

path = os.curdir
filepath = os.path.join(path, "infixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv('USER', 'anonymous')

while True:
    
    if not arguments:
        operation = input("Operacao: ")
        n1 = input("Numero 1: ")
        n2 = input("Numero 2: ")
        arguments = [operation, n1, n2]
    elif len(arguments) != 3:
        print("Uso: infixcalc.py [operacao] [numero1] [numero2]")
        sys.exit(1)

    operation, *nums = arguments
    
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

    try:
        n1, n2 = validated_nums
    except ValueError as e:
        print(str(e))
        sys.exit(1)
    
    result = valid_operations[operation](n1, n2)
    print(f"O resultado é {result}")
       
    try:
        with open(filepath, "a") as log:
            log.write(
                f"{timestamp} - {user} - {operation}, {n1}, {n2} = {result}\n")
    except PermissionError as e:
        print(str(e))
        sys.exit(1)

    arguments = None
    perg = input("Deseja continuar? [Y/n]: ").strip().lower() 
    if perg != "y":
        break