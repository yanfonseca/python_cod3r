pessoas = [
    {'nome': 'João', 'idade': 11},
    {'nome': 'Maria', 'idade': 18},
    {'nome': 'José', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 19},
    {'nome': 'Tiago', 'idade': 9},
    {'nome': 'Gabriela', 'idade': 30},
    {'nome': 'Mariana', 'idade': 30}
]

# filter retorna verdadeiro ou falso - função filtro e iterable
menores = filter(lambda p: p['idade'] < 18, pessoas)
print(list(menores))

nomegrande = filter(lambda p: len(p['nome'])
                    >= 7 or p['nome'] == 'José', pessoas)
print(list(nomegrande))
