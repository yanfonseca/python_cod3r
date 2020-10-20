def funcao():
    return 'teste'


class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'

    # atributo
    def __init__(self, nome):
        self.nome = nome
        self.teste = funcao()  # Testando se existe a possibilidade, não é uma boa prática
        self.teste2 = self.is_evoluido()
        self.vouprintar()
    # metodo de instancia

    def das_cavernas(self):
        # atributo de instância
        self.especie = 'Homo Neanderthalensis'
        return self

    @classmethod
    def vouprintar(cls):
        print('isso é um print')

    # Existem: método de instância, método de classe e método estático
    # metodo de instancia recebe instancia(self)
    # metodo de classe recebe o atributo de classe
    # metodo estatico nao recebe parametro

    # Não recebe nenhum parâmetro
    # Função estática é como uma função que está no escopo do módulo
    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    # É possível diferenciar o método de acordo com a classe que dispara o método
    @classmethod
    def is_evoluido(cls):  # convenção cls - cls polimorfismo
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    # Essa instância de classe será informada quando for usar a classe Humano
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):
    # Essa instância de classe será informada quando for usar a classe Humano
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    jose = HomoSapiens('Jose')
    # HomoSapiens.das_cavernas(jose)
    grokn = Neanderthal('Grokn')
    print(
        f'Evolução (a partir da classe): {", ".join(HomoSapiens.especies())}')
    print(f'Evolução (a partir da instância): {", ".join(jose.especies())}')

    print(f'Homo Sapiens evoluído? {HomoSapiens.is_evoluido()}')

    # nao seria possível ser feito com método estático
    print(f'Neaderthan evoluído? {Neanderthal.is_evoluido()}')
    print(Neanderthal.especie)

    print(f'José é evoluído? {jose.is_evoluido()}')
    print(f'Grokn é evoluído? {grokn.is_evoluido()}')

    print(jose.teste)
    print(jose.teste2)
