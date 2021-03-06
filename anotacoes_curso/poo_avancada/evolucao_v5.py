class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'

    # atributo
    def __init__(self, nome):
        self.nome = nome
        self._idade = None  # atributo privado

    # classe abstrata
    # pelo menos um dos metodos nao está implementado
    @property
    def inteligente(self):
        raise NotImplementedError('Propriedade não implementada')

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError('Idade deve ser um número positivo')
        self._idade = idade

    # metodo de instancia
    def das_cavernas(self):
        # atributo de instância
        self.especie = 'Homo Neanderthalensis'
        return self

    # metodo de instancia, metodo de classe e metodo estático
    # metodo de instancia recebe instancia(self)
    # metodo de classe recebe o atributo de classe
    # metodo estatico nao recebe nao parametro

    # Não recebe nenhum parâmetro
    # É como uma função que está no módulo
    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    # É possível diferenciar o método de acordo com a classe que dispara o método
    @classmethod
    def is_evoluido(cls):  # convenção cls - cls polimorfismo
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]

    # alterando o método da classe abstrata
    @property
    def inteligente(self):
        return False


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]

    # alterando o método da classe abstrata
    @property
    def inteligente(self):
        return True


if __name__ == '__main__':
    anonimo = Humano('John Doe')

    try:
        print(anonimo.inteligente)
    except NotImplementedError:
        print('propriedade abstrata')

    jose = HomoSapiens('José')
    print('{} da classe {}, inteligente: {}'
          .format(jose.nome, jose.__class__.__name__, jose.inteligente))
    grogn = Neanderthal('Grogn')
    print('{} da classe {}, inteligente: {}'
          .format(grogn.nome, grogn.__class__.__name__, grogn.inteligente))
