# shebang para UNIX #!/usr/local/bin/python3

import math

if __name__ == '__main__':

    raio = input('Informe o raio: ')  # Por padrão input guarda uma string
    print('Área', math.pi * float(raio) ** 2)
