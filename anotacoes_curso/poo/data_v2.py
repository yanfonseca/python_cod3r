class Data:

    # construtor - não é possível ter mais de um construtor
    # posso passar valores posicionais ou nomeados
    def __init__(self, dia=1, mes=1, ano=1970):
        print('opa!')
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data(5, 12, 2019)
d1.dia = 20  # é possível alterar
# d1.mes = 12
# d1.ano = 2019
print(d1)

# Se informado parâmetro nomeado, então, não pode usar mais posicional
d2 = Data(7, 11, ano=2020)
d2.dia = 7
# d2.mes = 11
# d2.ano = 2020

print(d2)

d3 = Data()
d3.mes = 9
print(d3)
