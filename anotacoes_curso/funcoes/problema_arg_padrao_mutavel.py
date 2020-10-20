def fibonacci(sequencia=[0, 1]):
    # Uso de mutáveis como valor default (armadilha)
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == '__main__':
    inicio = fibonacci()
    print(inicio, id(inicio))  # id() id de incio na memória do pc
    print(fibonacci(inicio))  # , id(fibonacci(inicio)))

    restart = fibonacci()
    # mesmo id() de início, isso causa problemas sequencia = ()
    # o id de restarte deveria ser diferente e não restarta a variável
    print(restart, id(restart))

    # só para mostrar o problema, restart não mostra o esperado
    assert restart == [0, 1, 1]
