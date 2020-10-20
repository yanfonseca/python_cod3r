# shebang para UNIX: #!/usr/local/bin/python3

import math
import sys
import errno


class TerminalColor:
    # ERRO = '\033[91m'
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


def circulo(raio):
    """
    Cálculo da área
    """
    return math.pi * float(raio) ** 2

    print('teste')


def help():
    print(f"""\
    É necessário informar o do cícrulo
    Sintaxe: {sys.argv[0]} <raio>""")


if __name__ == '__main__':

    if len(sys.argv) < 2:
        help()
        # sys.exit(1) #Exit termina o arquivo. sysexit(1) de forma bem sucedida, qualquer outro número mostra erro.
        sys.exit(errno.EPERM)  # errno.EPERM é o próprio número 1

    elif not sys.argv[1].isnumeric():
        help()
        print(TerminalColor.ERRO +
              'O raio deve ser um valor numérico' + TerminalColor.NORMAL)
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    area = circulo(raio)
    # print(sys.argv[0])
    print('Area do círculo: ', area)
    print(dir())
