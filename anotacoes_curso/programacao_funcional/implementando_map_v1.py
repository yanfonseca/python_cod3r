# implementação simplificada do map


def mapear(funcao, lista):

    for i in lista:
        print('passou')
        yield funcao(i)


if __name__ == '__main__':
    resultado = mapear(lambda x: x ** 2, [2, 3, 4])
    print(list(resultado))
    # print(next(resultado))
    # print(next(resultado))
    # print(next(resultado))
    # print(next(resultado)) #erro


# criar tupla com o map?
