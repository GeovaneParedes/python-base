#!/usr/bin/env python3
"""
Faca um programa que exibe ao usuario uma lista dos quartos disponiveis para 
alugar e o preco de cada quarto, esta informacao esta disponivel em um arquivo
de texto separado por virgulas.

'quartos.txt'
# codigo, name, price
1,Suite Master,500
2,Quarto Familia,200
3,Quarto C/casal,100
4,Quarto C/solteiro,50

O programa pergunta ao usuario o nome, qual o numero do quarto a ser reservado
e a quantidade de dias e no final exibe o valor estimado a ser pago.

O programa deve salvar esta escolha em outro arquivo contendo as reservas

'reserva.txt'
# cliente, quarto, dias
Bruno,3,12

Se outro usuario tentar reservar o mesmo quarto, o programa deve exibir uma 
mensagem informando que o quarto ja esta reservado.
"""
from pathlib import Path
import csv

rooms_path = Path("quartos.txt")
reservations_path = Path("reserva.txt")

print("Quartos disponiveis para reserva:")
ARQUIVO = Path("quartos.txt")
with ARQUIVO.open("r", encoding="utf-8") as file:
    reader = csv.reader(file)
    rooms_path = list(reader)
    for room in rooms_path[1:]:
        print(f"{room[0]} - {room[1]} - R$ {room[2]}")
        print("--" * 20)

name = input("Digite seu nome: ")
room_number = input("Digite o numero do quarto que deseja reservar: ")
days = int(input("Digite a quantidade de dias que deseja ficar: "))

reservations_path.touch(exist_ok=True)
with reservations_path.open("r+", encoding="utf-8") as file:
    reader = csv.reader(file)
    reservations = list(reader)
    reserved_rooms = [reservation[1] for reservation in reservations[1:]]
    if room_number in reserved_rooms:
        print("Desculpe, este quarto ja esta reservado.")
    else:
        room = next((room for room in rooms_path[1:] if room[0] == room_number)
                    , None)
        if room:
            price_per_day = float(room[2])
            total_price = price_per_day * days
            print(f"O valor total a ser pago e: R$ {total_price:.2f}")
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(["cliente", "quarto", "dias"])
            writer.writerow([name, room_number, days])
            print("Reserva realizada com sucesso!")
        else:
            print("Numero de quarto invalido.")