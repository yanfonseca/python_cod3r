

def fibonacci(sequencia=(0, 1)):
    # Uso de mutáveis como valor default (armadilha)
    # sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia + (sequencia[-1] + sequencia[-2],)


if __name__ == '__main__':
    inicio = fibonacci()
    print(inicio, id(inicio))  # id() id de incio na memória do pc
    print(fibonacci(inicio))
    restart = fibonacci()
    # mesmo id() de início, isso causa problemas sequencia = ()
    print(restart, id(restart))
