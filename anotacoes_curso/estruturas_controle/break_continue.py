from random import randint
for x in range(1, 11):
    if x % 2 == 0:
        continue  # interrompe e vai para a próxima repetição
    print(x)


for x in range(1, 11):
    if x == 5:
        break  # Interrompe a repetição
    print(x)

print('Acabou')

for j in range(2):
    print('Início >', j)
    for x in range(1, 11):
        if x == 5:
            break  # Interrompe a repetição interna
        print(x)

    print('Acabou - 1')
print('Acabou - 2')

for i in range(1, 11):
    if i == 6:
        break
    print(i)
else:
    print('fim')  # Não executa o else do for quando encontra um break
print('fim - fora')


def sortear_dado():
    return randint(1, 6)  # no randint o 6 também entra, é diferente do range


print('Começouo jogo')
for i in range(1, 7):
    sorteado = sortear_dado()
    if sorteado % 2 == 1:
        continue
    if sorteado == i:
        print('Acertou:', i)
        break
else:
    print('Não acertou')
