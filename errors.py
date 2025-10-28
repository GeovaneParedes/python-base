#!/usr/bin/env python3

import sys
import os
import logging
import time

log = logging.Logger("erros")
# EAFP - Easy to ASK Forgiveness than permission
# (E mais facil pedir perdao do que permisao)
def try_to_open_a_file(file_path, retry=1) -> list:
    if retry > 999:
        raise ValueError("Numero de tentativas muito alto")
    try:
        return open(file_path).readlines()
    except FileNotFoundError as e:
        log.error("ERROR: %s", e)
        time.sleep(2)
        if retry > 1:
            return try_to_open_a_file(file_path, retry=retry - 1)
    else:
        print("Sucesso!!!")
    finally:
        print("Executando o finally")
    return []

for line in try_to_open_a_file("names.txt", retry=5):
    print(line)