#!/usr/bin/env python3
'''Faca um programa que imprima todos os pares entre 1 e 200.

ex python3 pares.py

'''
pares = [n for n in range(1, 201) if n % 2 == 0]
print(pares)