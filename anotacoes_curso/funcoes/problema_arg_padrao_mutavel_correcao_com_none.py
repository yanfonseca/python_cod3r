def fibonacci(sequencia=None):  # none retorna false - not None -> True, not not None -> False
    sequencia = sequencia or [0, 1]  # resolvendo o problema
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == '__main__':
    inicio = fibonacci()
    print(inicio, id(inicio))  # id() id de incio na memória do pc
    print(fibonacci(inicio))
    restart = fibonacci()
    # mesmo id() de início, isso causa problemas sequencia = ()
    print(restart, id(restart))

    # só para mostrar o problema, restart não mostra o esperado
    assert restart == [0, 1, 1]
