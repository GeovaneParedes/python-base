#!/usr/bi/env python3

"""Exibir relátorio de crianças por atividades.

Imprimir a lista de crianças agrupadas por sala 
que frequentas cada uma das atividades.
"""
__version__ = "0.1.0"

sala1 = ["Erik", "Maria", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maria", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("Ingles", aula_ingles),
    ("Musica", aula_musica),
    ("Dança", aula_danca)
    ]

#Listar alunos em cada atividades por sala
for nome_atividade, atividade in atividades:
    
    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 40)
    atividade_sala1 = []
    atividade_sala2 = []

    for aluno in atividade:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)
    print(f"sala1 ", atividade_sala1)
    print(f"sala2 ", atividade_sala2)

    print("#" * 40)
    #print("Aula de Musica", aula_musica)
    #print("Aula de Dança", aula_danca)

