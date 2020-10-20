import sys
generator = (i ** 2 for i in range(10) if i % 2 == 0)

# print(list(generator))
# print(len(generator)) #Erro
print(generator)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
# print(next(generator)) #erro
print(next(generator, 'Fim do generator'))

generator = (i ** 2 for i in range(10) if i % 2 == 0)

for i in generator:
    print(i)

    print('item_em_memoria', sys.getsizeof(i))

generator = (i ** 2 for i in range(10) if i % 2 == 0)
print('Lista_em_memoria', sys.getsizeof(list(generator)))
