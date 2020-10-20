# shebang para UNIX #!/usr/local/bin/python3

import math


def circulo(raio):
    area = math.pi * float(raio) ** 2
    print('Área', area)
    return area


if __name__ == '__main__':
    raio = input('Informe o raio: ')  # Por padrão input guarda uma string
    circulo(raio)
