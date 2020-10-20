from locale import setlocale, LC_ALL  # LC é um grupo
from calendar import mdays, month_name
from functools import reduce


# setlocal pode alterar currency, month e etc de acordo com  o país
print(LC_ALL)
setlocale(LC_ALL, 'pt_BR')
print(month_name[1])

print('Lista com os meses do ano com 31 dias\n')


def mes_com_31(mes):
    return mdays[mes] == 31


def get_nome_mes(mes):
    return month_name[mes]


def juntar_meses(todos, nome_mes):
    return f'{todos}\n- {nome_mes}'


# abordagem declarativa
print(reduce(juntar_meses,
             map(get_nome_mes, filter(mes_com_31, range(1, 13))),
             'Mes com 31 dias'))
