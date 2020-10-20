#[f(x) for x in sequence if condition]
#[f(x) if condition else g(x) for x in sequence]


def get_tipo_dia(dia):
    dias = {
        (1, 7): 'Fim de semana',
        tuple(range(2, 7)): 'Dias de semana'
    }

    saida = 0
    for numeros, tipo in dias.items():
        if dia in numeros:
            return tipo
        elif dia not in numeros:
            saida += 1
            if saida == 2:
                return '** dia inválido **'


if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'dia:{dia}: {get_tipo_dia(dia)}')
