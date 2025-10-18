#!/usr/bin/env python3 
"""Imprimi a mensaguem de um email
Nao mande spam, por favor."""
__version__ = "0.1.0"


import os
import sys
import smtplib
from email.mime.text import MIMEText

arguments = sys.argv[1:]
if not arguments:
    print("Informe o nome do arquivo de emails.")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename)
templatename = os.path.join(path, templatename)

with smtplib.SMTP("localhost", 8025) as server:
    for line in open(filepath):
        name, email = line.split(",")

        text = (
            open(templatename).read()
            % {
                "nome": name,
                "produto": "curso de Python",
                "texto" : "Aprenda Python conosco",
                "link": "https://t.me/pythonpraticando",
                "quantidade": 5,
                "preco": 49.90,
            }
        )

        from_ = "devgegepythonjr@gmailcom"
        to = ", ".join([email])
        message = MIMEText(text)
        message["Subject"] = "Aprenda Python conosco!"
        message["From"] = from_ 
        message["To"] = to

        server.sendmail(from_, [email], message.as_string())
        