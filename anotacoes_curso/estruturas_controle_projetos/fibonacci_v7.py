# #!/usr/local/bin/python3

# 0,1,1,2,3,5,8...


def fibonacci(quantidade):
    resultado = [0, 1]

    # Essa estrutura me parece mais comum
    for _ in range(2, quantidade):
        resultado.append(sum(resultado[-2:]))

    return resultado

    # while len(resultado) != quantidade:
    #     resultado.append(sum(resultado[-2:]))
    # return resultado


if __name__ == '__main__':
    for fib in fibonacci(20):
        print(fib)
