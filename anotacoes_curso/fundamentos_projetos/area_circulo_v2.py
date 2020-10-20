# shebang para UNIX #!/usr/local/bin/python3

import math

raio = input('Informe o raio: ')  # Por padrão input guarda uma string
print('Área', math.pi * float(raio) ** 2)


print('Nome do módulo', dir())
print('Nome do módulo', __name__)  # execuçao de um .py
print('Nome do pacote', __package__)
