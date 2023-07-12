# lab1 by heusmat

dia_mes = int(input())
dia_semana = input()
valor = float(input())

if dia_mes % 7 == 0:
    valor = valor * 0.50
else:
    if dia_semana == 'sexta-feira':
        valor = valor * 0.75
    else:
        if valor >= dia_mes:
            valor = valor - dia_mes
        else:
            valor = 0

print(f'{valor:.2f}')

if dia_semana == 'segunda-feira':
    print('É um dia terrível, você não devia ter saído da cama.')
else:
    if dia_semana == 'sábado' or dia_semana == 'domingo':
        print('Agradecemos a preferência, tenha um ótimo fim de semana!')
    else:
        print(f'Agradecemos a preferência, tenha uma ótima {dia_semana}!')
