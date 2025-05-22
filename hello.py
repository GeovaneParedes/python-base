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
__version__="0.0.1"
__author__="DevGege"
__license__="Unlincense"

import os

current_language = os.getenv("LANG", "en_US")[:5]
msg = "Hello, World!"
if current_language == "pt_BR":
    msg = "Ola, Mundo"
elif current_language == "en_US":
    msg = "Hello, World!"
    
print(msg)

print('My name is Geovane Paredes')
print('I am a software engineer Python developer')
print('I am developing python jr')
print('I am learning how to use Git and GitHub')
