#!/usr/bin/env python3
def repete_vogais(word):
    """Retorna a palavra com as vogais repetidas"""
    final_word = ''
   #for index, letter in enumerate(word):
       #print(f"{index=}, {letter=}")
    for letter in word:
        if letter.lower() in "aeiouãáàâéêíóôõú":
            final_word += letter * 2 # A falta do operador de atribuição composto foi o erro
        else:
            final_word += letter # A falta do operador de atribuição composto foi o erro
       #print(f"{final_word=}")
    return final_word


print(repete_vogais("Banana"))
