def executar(funcao, ponto='.'):
    if callable(funcao):
        funcao(ponto)
    else:
        print('Não callable!')


def bom_dia(ponto):
    print('Bom dia' + ponto)


def boa_tarde(ponto):
    print('Bom tarde' + ponto)


if __name__ == '__main__':
    executar(bom_dia, '!')
    executar(boa_tarde, '!')
    executar(1)
