import os
import re

prefixo_base = "#D"
expressao_remover = "YouTube"

# Caminho da pasta onde estão os vídeos
pasta = "."

# Lista os vídeos e ordena para ter uma sequência previsível
videos = [f for f in os.listdir(pasta) if f.lower().endswith(('.mp4', '.avi', '.mkv', '.mov'))]
videos.sort()

for indice, nome_original in enumerate(videos, start=1):
    # Remove a expressão "YouTube"
    nome_novo = nome_original.replace(expressao_remover, "")

    # Remove espaços extras
    nome_novo = " ".join(nome_novo.split())

    # Troca espaços por underline
    nome_novo = nome_novo.replace(" ", "_")

    # Remove as 6 primeiras caracteres
    nome_novo = nome_novo[6:]

    # Remove o '-_' antes da extensão do arquivo
    nome_novo = re.sub(r'-_(\.[a-zA-Z0-9]+)$', r'\1', nome_novo)

    # Adiciona prefixo sequencial (ex.: #D001_)
    prefixo = f"{prefixo_base}{indice:03d}_"
    nome_novo = prefixo + nome_novo

    caminho_antigo = os.path.join(pasta, nome_original)
    caminho_novo = os.path.join(pasta, nome_novo)

    print(f"Renomeando:\n  {nome_original}\npara\n  {nome_novo}\n")
    os.rename(caminho_antigo, caminho_novo)

