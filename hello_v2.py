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

arguments = {"lang": None, "count": 1}
msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!"
}

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
        sys.exit(1)
    arguments[key] = value

while True:
    current_language = arguments["lang"]
    if current_language is None:
        if "LANG" in os.environ:
            current_language = os.getenv("LANG")
        else:
            current_language = input("Choose a language (ex: pt_BR, en_US): ").strip()

    current_language = current_language[:5]
    try:
        message = msg[current_language]
    except KeyError:
        print(f"[ERROR] Language '{current_language}' is invalid.")
        print(f"Choose from: {list(msg.keys())}")
        continue

    count = arguments.get("count")
    try:
        count = int(count)
    except (TypeError, ValueError):
        count = 1

    print(message * count)

    resp = input("Do you want to continue? [y/N]: ")
    if resp.lower() != 'y':
        break

    arguments["lang"] = input("Which language do you want the greeting in? (ex: pt_BR): ").strip()
