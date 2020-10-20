def soma_2(a, b):
    return a + b


def soma_3(a, b, c):
    return a + b + c


def soma_n(*numeros):  # Recebe desempacotado e empacota com *
    soma = 0
    # print(type(numeros)) #transforma em tupla
    for n in numeros:
        soma += n
    return soma


def soma_n2(*numeros):
    return sum(list(numeros))


if __name__ == '__main__':
    print(soma_2(2, 3))
    print(soma_3(2, 4, 6))

    # packing
    # Informa dados desempacotados
    print(soma_n(1))
    print(soma_n(1, 1))
    print(soma_n(1, 11, 1, 1, 1, 1))

    # unpacking
    # Informa dados empacotados
    tupla_num = (1, 2, 3)
    # Desempacota com * e na entrada da função serão empacotados novamente
    print(soma_n(*tupla_num))

    # unpacking
    list_num = [1, 2, 3]
    # Desempacota com * e na entrada da função serão empacotados novamente
    print(soma_n(*list_num))

    print('soma_n2')
    # packing
    print(soma_n2(1, 11, 1, 1, 1, 1))
    # unpaking
    list_num = [1, 2, 3]
    print(soma_n2(*list_num))
