"""Exemplos de funcoes
f(x) = 5 * (x / 2)
"""
def f(x):
    result = 5 * (x // 2)
    return result

valor = f(10)

print(valor)
print(valor == 25)


def heron(a, b, c):
    """Calcula a area de um triangulo"""
    perimeter = a + b + c
    s = perimeter / 2
    area = s * (s - a) * (s - b) * (s - c)
    return area ** 0.5 # math.sqrt(area)

triangulos = [
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (12, 35, 37),
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (12, 35, 37)
]

for t in triangulos:
    area = heron(t[0], t[1], t[2])
    print(f"A area do Triangulo e: {area}")

