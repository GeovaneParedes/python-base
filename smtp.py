#!/usr/bin/env python3
"""
Exemplos de envio de e-mail

"""
import smtplib
import asyncore
import asynchat

SERVER = "localhost"
PORT = 8025

FROM =  "devgegepythonjr@gmail.com"
TO =  ["geovaneparedes2@gmail.com"]
SUBJECT = "Meu e-mail via terminal usando python"
TEXT = """
Este e o e-mail enviado pelo python. Enviado pelo meu IPHONE 200x
<b>Ola meu brother</b>
"""

message = f"""\
From: {FROM}
TO: {TO}
Subject: {SUBJECT}
{TEXT}
"""

with smtplib.SMTP(host=SERVER, port=PORT) as server:
    server.sendmail(FROM, TO, message.encode('utf-8'))
