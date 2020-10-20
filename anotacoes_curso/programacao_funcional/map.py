lista_1 = [1, 2, 3]

dobro = map(lambda x: x * 2, lista_1)

print(list(dobro))

lista_2 = [
    {'nome': 'João', 'idade': 31},
    {'nome': 'Maria', 'idade': 35},
    {'nome': 'José', 'idade': 39},
]


nomes = map(lambda p: p['nome'], lista_2)
print(list(nomes))
idades = map(lambda p: p['idade'], lista_2)
print(sum(idades))

# desafio

frases = map(lambda p: f'{p["nome"]} tem {p["idade"]} anos', lista_2)
print(type(frases))
print(list(frases))

# a lista original não se altera usando o paradigma funcional, usando map


# testes

def tabuada():
    for i in range(1, 11):
        yield list(map(lambda num1, num2: f'{num1}x{num2}={num1 * num2}', [i] * 10, range(1, 11)))


for i in tabuada():
    print(i)
