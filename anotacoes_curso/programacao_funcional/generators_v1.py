# criar generator, não usar o resultado genarator de um list_comprehension por exemplo
# generator é uma funçao com retornos parciais
# funciona com uma função com memória
# sabe do último retorno e do próximo

# yield == produzir


def cores_arco_iris():
    yield 'vermelho'
    yield 'laranja'
    yield 'amarelo'
    yield 'verde'
    yield 'azul'
    yield 'índigo'
    yield 'violeta'


j
if __name__ == '__main__':
    generator = cores_arco_iris()
    print(type(generator))

    while True:
        print(next(generator))
