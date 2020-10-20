# #!/usr/local/bin/python3

# tupla1 + tuple2 = concatena as tuplas


def fibonacci(quantidade, sequencia=(0, 1)):
    # Importante: Condição de parada
    if len(sequencia) == quantidade:
        return sequencia
    return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]), ))


if __name__ == '__main__':

    for fib in fibonacci(10):
        print(fib)
