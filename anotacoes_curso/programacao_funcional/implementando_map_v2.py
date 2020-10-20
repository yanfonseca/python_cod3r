# implementação simplificada do map


def mapear(funcao, lista):
    return (funcao(i) for i in lista)


if __name__ == '__main__':
    resultado = mapear(lambda x: x ** 2, [2, 3, 4])
    print(list(resultado))
    # print(next(resultado))
    # print(next(resultado))
    # print(next(resultado))
    # print(next(resultado)) #erro


# criar tupla com o map?
