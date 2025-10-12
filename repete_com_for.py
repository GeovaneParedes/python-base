#!/usr/bin/env python3

# for loops
original = [1, 2, 3]

dobrado = []
for n in original:
    dobrado.append(n * 2)
print(dobrado)

# list comprehensions
dobrado = [n * 2 for n in original]
print(dobrado)

# Dict comprehension
dados = {
    line.split(":")[0]: line.split(":")[1].strip()
    for line in open("notes.txt")
    if ":" in line
}
print(dados)
dados = {}
for line in open("notes.txt"):
    if ':' in line:
        key, valor = line.split(":")
        dados[key] = valor.strip()

print(dados)
