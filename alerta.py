#!/usr/bin/env python3
'''
Alarme de Temperatura

Faca um script que pergunta ao usuario a temperatura atual e o indice de 
umidade do ar sendo que sera exibida uma mensagem de alerta dependendo 
das condicoes:

temp maior 45: ALERTA!!! Perigo calor extremo
temp vezes 3 for maior ou igual a umidade: ALERTA!!! Perigo de calor umido
temp entre 10 e 30: Normal
temp entre 0 e 10: Frio
temp menor que 0: ALERTA!!! Frio extremo, cuidado com a hipotermia
'''
temp = float(input('Informe a temperatura atual: '))
umidade = float(input('Informe o indice de umidade do ar: '))
if temp > 45:
    print('ALERTA!!! Perigo calor extremo')
elif temp * 3 >= umidade:
    print('ALERTA!!! Perigo de calor umido')
elif 10 <= temp <= 30:
    print('Normal')
elif 0 <= temp < 10:
    print('Frio')
else:
    print('ALERTA!!! Frio extremo, cuidado com a hipotermia')