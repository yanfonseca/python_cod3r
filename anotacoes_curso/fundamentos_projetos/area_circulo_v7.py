# shebang para UNIX: #!/usr/local/bin/python3

import math
import sys


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

    else:
        raio = sys.argv[1]
        area = circulo(raio)
        # print(sys.argv[0])
        print('Area do círculo: ', area)
