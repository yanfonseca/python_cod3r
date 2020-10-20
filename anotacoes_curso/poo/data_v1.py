class Data:  # DataHospital DataNascimento
    # pass

    # __str__ método especial
    # método mágico suportado por todos objetos do python
    # já converte direto para string
    def __str__(self):  # todo método tem a palavra self(objeto acessado no momento)
        return f'{self.dia}/{self.mes}/{self.ano}'

    def to_string(self):  # todo método tem a palavra self(objeto acessado no momento)
        return f'{self.dia}/{self.mes}/{self.ano}'


# chama método construtor
d1 = Data()  # é possível criar atributos porque python é uma linguagem dinâmica
d1.dia = 5
d1.mes = 12
d1.ano = 2019
print(d1.to_string())
print(d1)

d2 = Data()
d2.dia = 7
d2.mes = 11
d2.ano = 2020  # Todos os atributos precisam ser criados antes do print

print(d2.to_string())
print(d2)
print('#')
print(f'{d1.dia}/{d1.mes}/{d1.ano}')
