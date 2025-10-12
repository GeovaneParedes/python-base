#!/usr/bin/env python3

import os
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

"""
log.debug("Mensagem pro Dev, qe, sysadmin")
log.info("Mensagem geral para usuarios")
log.warning("Aviso que nao causa erro")
log.error("Erro que afeta um unica execucao")
log.critical("Erro geral: Banco de dados sumiu") # root logger
"""
print("-" * 20)

try:
    1 / 0
except ZeroDivisionError as e:
    log.error("Deu erro %s", str(e))