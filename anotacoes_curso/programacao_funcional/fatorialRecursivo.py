from functools import reduce

# usando programacao funcional


def fatorial(numero):
    return reduce(lambda num1, num2: num1 * num2, range(1, numero+1), 1)


# usando funcao recursiva
# A partir da chamada recursiva 997 o programa trava.
# É possível alterar essa quantidade.
def fatorial2(numero):
    return numero * (fatorial2(numero - 1) if (numero-1) > 1 else 1)


if __name__ == '__main__':
    print(f'10! = {fatorial(10)}')
    print(f'10! = {fatorial2(10)}')
