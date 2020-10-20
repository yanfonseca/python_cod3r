
# break, continue funcionam dentro de estruturas loop
# Para sair da função recursiva é preciso usar o return,
# mas a função pode não retornar nada


def imprimir(maximo, atual):
    if atual < maximo:
        print(atual)
        imprimir(maximo, atual + 1)
    return


imprimir(1000, 1)  # a condição de parada de uma funcao recursiva é 997
