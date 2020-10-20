#[f(x) for x in sequence if condition]
#[f(x) if condition else g(x) for x in sequence]

#numeros, tipo = dias.items()
#print(numeros, tipo)

teste = [i*2 if i % 2 == 0 else 'erro' for i in range(10)]
print(teste)


def get_tipo_dia(dia):
    dias = {
        (1, 7): 'Fim de semana',
        tuple(range(2, 7)): 'Dias de semana'
    }
    dia_escolhido = (tipo for numeros, tipo in dias.items() if dia in numeros)
    return next(dia_escolhido, '** dia inválido **')


if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{dia}: {get_tipo_dia(dia)}')
