#!/usr/bin/env python3

"""
Hello World Multi Linguas

Dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspodente.
Usage:
Ter uma variavel de ambiente LANG devidamente configurada ex: export LANG=pt_br
Exe:
python3 hello.py ou ./hello.py
"""
__version__="0.1.3"
__author__="DevGege"
__license__="Unlincense"

import os
import sys

arguments = {
    "lang": None,
    "count": 1,
}
for arg in sys.argv[1:]:
    #TODO Tratar ValueError
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalion Option `{key}`")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    #TODO: Usar repeticao
    else:
        current_language = input("Choose a Language:")
current_language = current_language[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr-FR": "Bonjour, Monde!"
}
#Ordem Complexidade O(n)
print(msg[current_language] * int(arguments["count"]))

print('My name is Geovane Paredes')
print('I am a software engineer Python developer')
print('I am developing python jr')
print('I am learning how to use Git and GitHub')
