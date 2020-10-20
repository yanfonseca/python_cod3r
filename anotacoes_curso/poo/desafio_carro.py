class Carro:
    def __init__(self, velocidade_maxima):
        self.velocidade_maxima = velocidade_maxima
        self.velocidade_atual = 0

    def acelerar(self, delta=5):
        nova = self.velocidade_atual + delta
        maxima = self.velocidade_maxima
        self.velocidade_atual = nova if nova <= maxima else maxima
        return self.velocidade_atual

    def frear(self, delta=5):
        nova = self.velocidade_atual - delta
        self.velocidade_atual = nova if nova >= 0 else 0
        return self.velocidade_atual


if __name__ == '__main__':
    c1 = Carro(180)  # 0 e velocidade máx

    print('acelerar')
    for i in range(25):
        print(i, c1.acelerar(8))
    print('frear')
    for i in range(10):
        print(i, c1.frear(delta=20))  # delta padrao é 5
