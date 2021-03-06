# shebang para UNIX: #!/usr/local/bin/python3

import math
import sys
import errno


def circulo(raio):
    """
    Cálculo da área
    """
    return math.pi * float(raio) ** 2


def help():
    print(f"""\
    É necessário informar o raio do círculo
    Sintaxe: {sys.argv[0]} <raio>""")


if __name__ == '__main__':

    if len(sys.argv) < 2:
        help()
        # sys.exit(1) #Exit termina o arquivo. sysexit(1) de forma bem sucedida, qualquer outro número mostra erro.
        sys.exit(errno.EPERM)  # errno.EPERM é o próprio número 1

    elif not sys.argv[1].isnumeric():
        help()
        print('O raio deve ser um valor numérico')
        sys.exit(errno.EINVAL)

    else:
        raio = sys.argv[1]
        area = circulo(raio)
        # print(sys.argv[0])
        print('Area do círculo: ', area)
