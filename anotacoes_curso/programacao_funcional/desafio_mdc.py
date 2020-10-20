def mdc(numeros):
    def calc(divisor):
        return divisor if sum(map(lambda x: x % divisor, numeros)) == 0 \
            else calc(divisor - 1)

    return calc(max(numeros))


if __name__ == '__main__':
    print(mdc([21, 7]))  # 7
    print(mdc([125, 40]))  # 5
    print(mdc([7, 9]))  # 5
    print(mdc([6, 9, 12, 36]))


# regras para mdc
