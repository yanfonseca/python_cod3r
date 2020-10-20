palavra = 'paralelepípedo'

for letra in palavra:
    print(letra, end=',')
print('Fim')
print('Nova linha')

aprovados = ['Rafa', 'Paula', 'Renan', 'Mari']

for nome in aprovados:
    print(nome)

for posicao, nome in enumerate(aprovados):
    print(f'posição {posicao}, nome {nome}')

aprovados = tuple(aprovados)

for posicao, nome in enumerate(aprovados):
    print(f'posição {posicao}, nome {nome}')

for numero in {2, 1, 3, 4, 5}:
    print(numero)


produto = {'nome': 'Caneta', 'preco': 15}

for chave in produto:
    print(chave)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(chave, valor)
