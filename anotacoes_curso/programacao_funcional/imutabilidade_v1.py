from locale import setlocale, LC_ALL  # LC é um grupo
from calendar import mdays, month_name
from functools import reduce


# setlocal pode alterar currency, month e etc de acordo com  o país
print(LC_ALL)
setlocale(LC_ALL, 'pt_BR')
print(month_name[1])

print('Lista com os meses do ano com 31 dias\n')

# 1. Pegar os índices dos meses com 31 dias - filter
# 2. Transformar índice em nome - map
# 3. Juntar e imprimir - reduce

meses_31 = filter(lambda mes: mdays[mes] == 31, range(1, 13))
meses_nomes = map(lambda dia: month_name[dia], meses_31)
juntar_meses = reduce(
    lambda todos, nome_mes: f'{todos}\n- {nome_mes.capitalize()}', meses_nomes, 'Meses com 31 dias:')

print(juntar_meses)

print(
    reduce(
        lambda todos, nome_mes: f'{todos}\n- {nome_mes.capitalize()}',
        map(
            lambda dia: month_name[dia],
            filter(
                lambda mes: mdays[mes] == 31, range(1, 13)
            )
        ), 'Meses com 31 dias:')

)


meses_nomes = [meses for meses in month_name]
meses_dias = [dias for dias in mdays]

print('Lista com os meses do ano com 31 dias')
[print(f'- {mes.capitalize()}')
 for dia, mes in zip(meses_dias, meses_nomes) if dia == 31]
