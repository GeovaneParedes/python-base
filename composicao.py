"""Imprime apenas os nomes iniciados com a letra b"""

names = [
    "Bruno",
    "Joao",
    "Bernardo",
    "Barbara",
    "Brian",
]

print("-----")
print("Estilo Funcional")
print(*list(filter(lambda text: text[0].lower() == "b", names)), sep="\n")
print("-----")
print("Estilo Imperativo")
def starts_with_b(text):
    return text[0].lower() == "b"
filtro = filter(starts_with_b, names)
filtro = list(filtro)
for name in filtro:
    print(name)
