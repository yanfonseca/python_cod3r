def multiplicar(x):
    def calcular(y):
        return x * y
    return calcular


if __name__ == '__main__':
    dobro = multiplicar(2)
    print(dobro(4))

    triplo = multiplicar(3)
    print(triplo(4))
