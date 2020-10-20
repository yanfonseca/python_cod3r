class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'

    # atributo
    def __init__(self, nome):
        self.nome = nome
        # atributo privado(existe a possibilidade de acesso mas deve ser evitado)
        self._idade = None

    def get_idade(self):
        return self._idade

    def set_idade(self, idade):
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


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    jose = HomoSapiens('Jose')
    jose.set_idade(40)
    print(f'Nome: {jose.nome}, Idade: {jose.get_idade()}')
