#!/usr/bin/env python3
'''
Repete vogais

Faca um programa que pede ao usuario que digite uma ou mais palavras e imprime
cada uma das palavras com suas vogais duplicadas.

ex:
python3 repete_vogais.py
'Digite uma palavra (ou enter para sair): ' Python
'Digite uma palavra (ou enter para sair): ' Bruno
'Digite uma palavra (ou enter para sair): ' <enter>
Pythoon
Bruunoo
'''
vogais = 'aeiouAEIOU'
while True:
    palavra = input("Digite uma palavra (ou enter para sair): ")
    if palavra == '':
        break
    nova_palavra = ''
    for letra in palavra:
        if letra in vogais:
            nova_palavra += letra * 2
        else:
            nova_palavra += letra
    print(nova_palavra)
 

