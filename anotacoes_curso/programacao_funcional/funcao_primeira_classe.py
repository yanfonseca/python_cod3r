def dobro(x):
    return x*2


def quadrado(x):
    return x ** 2


if __name__ == '__main__':
    funcs = [dobro, quadrado] * 5
    l = len(funcs)

    print(l, len(range(1, 11)))
    for numero, func in zip(range(1, 11), funcs):

        print(f'O {func.__name__} de {numero} é {func(numero)}')
