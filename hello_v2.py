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
import logging

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

log = logging.Logger("Geovane", log_level)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)

ch.setFormatter(fmt)
log.addHandler(ch)

arguments = {"lang": None,"count": 1}

for arg in sys.argv[1:]:
    try:
        key, value = arg.split("=")
    except ValueError as e:
        log.error(
            "You need to use '=', you passed %s, try --key=value: %s",
            arg,
            str(e)
        )
        sys.exit(1)

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
# LBYL

try:
    message = msg[current_language]
except KeyError as e:
    print(f"[ERROR] {str(e)}")
    print(f"Language is Invalid, choose from: {list(msg.keys())}")
    sys.exit(1)
print(message * int(arguments["count"]))
 
print('My name is Geovane Paredes')
print('I am a software engineer Python developer')
print('I am developing python jr')
print('I am learning how to use Git and GitHub')
