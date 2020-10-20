# shebang para UNIX #!/usr/local/bin/python3
# shebang no windows #! python
# -*- coding: utf-8 -*-

import math
print(dir())

raio = input('Informe o raio: ')  # Por padrão input guarda uma string
print(type(raio))
print('Área', math.pi * float(raio) ** 2)
