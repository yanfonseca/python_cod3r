
class ClassSimples:
    # atributo de classe: estático, não precisa criar um objeto
    # atributo é o mesmo para todos os objetos

    contador = 0

    def __init__(self):
        # self.__class__.contador += 1 #alternativa
        self.contar()

    def teste(self):
        self.contar()

    @classmethod
    def contar(cls):
        cls.contador += 1


if __name__ == '__main__':
    lista = [ClassSimples(), ClassSimples()]
    print(ClassSimples.contador)  # esperado 2

    print(lista[0].teste())
    print(ClassSimples.contador)
