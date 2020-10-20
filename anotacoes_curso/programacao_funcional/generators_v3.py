# usando o while o passo anterior fica na memória


def sequence():
    numero = 0

    while True:
        numero += 1
        yield numero


if __name__ == '__main__':
    seq = sequence()
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
