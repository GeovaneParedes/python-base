#!/usr/bin/env python3

import sys
import os
import logging

log = logging.Logger("erros")
# EAFP - Easy to ASK Forgiveness than permission
# (E mais facil pedir perdao do que permisao)
def try_to_open_a_file(file_path, retry=1) -> list:
    for attempt in range(1, retry + 1):
        try:
            return open(file_path).readlines()
        except FileNotFoundError as e:
            log.error("ERROR: %s", e)
        else:
            print("Sucesso!!!")
            return file
        finally:
            print("Executando o finally")
    return []

for line in try_to_open_a_file("names.txt"):
    print(line)