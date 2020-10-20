from functools import reduce

# lista gerar dicionario, lista lista, lista um número
pessoas = [

    {'nome': 'João', 'idade': 11},
    {'nome': 'Maria', 'idade': 18},
    {'nome': 'José', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 19},
    {'nome': 'Tiago', 'idade': 9},
    {'nome': 'Gabriela', 'idade': 30},
    {'nome': 'Mariana', 'idade': 30}
]


# reduce tem um acumulador
# soma_idades = reduce(lambda idades, p: idades + p['idade'], pessoas, 0)
# print(soma_idades)

# idades = map(lambda p: p['idade'], pessoas)
# menores = filter(lambda idade: idade < 18, idades)
# soma_idades = reduce(lambda idades, p: idades + p, menores, 0)
# print(soma_idades)


# testes
frase = 'Essa é a minha frase, atenção na nova concatenação!'
frase = frase.split(' ')
print(frase)
concatenadas = reduce(lambda texto1, texto2: texto1 + ' ' +
                      texto2, frase, 'Adicionei texto no início.')
print(str(concatenadas))

print(" ".join(frase))
