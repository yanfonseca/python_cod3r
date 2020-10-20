# shebang para UNIX #!/usr/local/bin/python3

import math


def circulo(raio):
    return math.pi * float(raio) ** 2


if __name__ == '__main__':
    raio = input('Informe o raio: ')  # Por padrão input guarda uma string
    area = circulo(raio)
    print('Area do círculo: ', area)
