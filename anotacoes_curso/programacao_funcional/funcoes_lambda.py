compras = (
    {'quantidade': 2, 'preco': 10},
    {'quantidade': 4, 'preco': 15},
    {'quantidade': 6, 'preco': 20},
)

totais = tuple(
    map(
        lambda compra: compra['quantidade'] * compra['preco'],
        compras
    )
)

print('Preços totais', totais)
print('Preços totais', sum(totais))

# bom usar em funções específicas
# lambda funcao anônima

print(type(compras))
print(type(compras[0]))
