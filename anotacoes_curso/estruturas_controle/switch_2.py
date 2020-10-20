def get_tipo_dia1(dia):

    dias = {
        1: 'Fim de semana',
        2: 'Dia de semana',
        3: 'Dia de semana',
        4: 'Dia de semana',
        5: 'Dia de semana',
        6: 'Dia de semana',
        7: 'Fim de semana'
    }

    return dias.get(dia, '** Não existe esse dia **')


def get_tipo_dia2(dia):

    if dia in [1, 6]:
        return 'Fim de semana'

    elif dia in range(2, 7):
        return 'Dia de semana'

    else:
        return '** Não existe esse dia **'


def get_tipo_dia3(dia):

    return 'Fim de semana' if dia in [1, 6] else ('Dia de semana' if dia in range(2, 7) else '** Não existe esse dia **')


if __name__ == '__main__':
    for dia in range(8):
        print(f'{dia}: f1-{get_tipo_dia1(dia)}')
        print(f'{dia}: f2-{get_tipo_dia2(dia)}')
        print(f'{dia}: f3-{get_tipo_dia3(dia)}')
