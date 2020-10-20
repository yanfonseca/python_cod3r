def soma(a, b):
    def soma_c(c):
        return a + b + c
    return soma_c


soma_5 = soma(2, 3)  # a,b
print(soma_5(5))  # c
print(soma(1, 3)(5))


soma_5 = soma(a=2, b=3)
print(soma_5(c=5))
print(soma(1, 3)(5))
