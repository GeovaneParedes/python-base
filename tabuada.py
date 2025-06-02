#!/usr/bin/env python
"""Imprimi a a tabuada de 1 a 10.

---Tabuada do 1---
    1 x 1 = 1
    1 x 2 = 2
...
###################
___version__ = "0.1.1"
__author__ = "DevGege"
"""

numeros = list(range(1, 11))
for n1 in numeros:
    print("{:-^20}".format(f"Tabuada do {n1}"))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^20}".format(f"{n1} x {n2} = {resultado}"))
    print()
    print("#" * 20)
