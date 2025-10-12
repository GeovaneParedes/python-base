#!/usr/bin/env python3

import sys
import os

# EAFP - Easy to ASK Forgiveness than permission
# (E mais facil pedir perdao do que permisao)

try:
    names = open("names.txt").readlines() # FileNotFoundError
except FileNotFoundError as e: # Error por falta do arquivo
    print("{str(e)}.")
    sys.exit(1)
    # TODO: Usar Retry
else:
    print("Sucesso!!!")
finally:
    print("Execute isso sempre!")
try:
    print(names[2])
except IndexError as e: # Erro indice
    print(f"{str(e)}.")
    sys.exit(1)