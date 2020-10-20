class Humano:
    # atributo de classe
    # compartilha o valor com todos os objetos
    especie = 'Homo Sapiens'

    # atributo de instância
    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        # atributo de instância
        self.especie = 'Homo Neanderthalensis'
        return self  # para ser possível o encadeamento


if __name__ == '__main__':
    jose = Humano('José')
    #grokn = Humano('Grokn')

    # Se a funcao retorna self, pode usar o encadeamento
    grokn = Humano('Grokn').das_cavernas()
    # print(grokn.das_cavernas() is None)

    print(f'Humano.especie: {Humano.especie}')
    print(f'jose.especie: {jose.especie}')
    print(f'grokn.especie: {grokn.especie}')
