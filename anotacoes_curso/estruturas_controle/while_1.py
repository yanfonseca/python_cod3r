# while True:
#     print('Vai demorar...')

# Para quantidade indefinida.

from random import randint

num_informado = -1
num_secreto = randint(0, 9)

while num_informado != num_secreto:
    num_informado = int(input('Informe o número: '))

print('Número secreto {} foi encontrado!'.format(num_secreto))
