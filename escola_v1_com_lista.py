#!/usr/bin/env python3

"""Exibir relatório de crianças por atividades.

Imprimir a lista de crianças agrupadas por sala 
que frequentam cada uma das atividades.
"""
__version__ = "0.1.0"

sala1 = ["Erik", "Maria", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maria", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("Inglês", aula_ingles),
    ("Música", aula_musica),
    ("Dança", aula_danca)
]

def alunos_por_sala(atividade, sala):
    """Retorna os alunos da sala que participam da atividade."""
    return [aluno for aluno in atividade if aluno in sala]

for nome_atividade, atividade in atividades:
    print(f"\nAlunos da atividade {nome_atividade}")
    print("-" * 40)
    print("Sala 1:", ", ".join(alunos_por_sala(atividade, sala1)) or "Nenhum")
    print("Sala 2:", ", ".join(alunos_por_sala(atividade, sala2)) or "Nenhum")
    print("#" * 40)