compras = (
    {'quantidade': 2, 'preco': 10},
    {'quantidade': 4, 'preco': 15},
    {'quantidade': 6, 'preco': 20},
)


def calc_preco_total(compra):
    return compra['quantidade'] * compra['preco']


totais = tuple(
    map(
        calc_preco_total,
        compras
    )
)

print('Preços totais', totais)
print('Preços totais', sum(totais))

# bom usar em funções específicas
