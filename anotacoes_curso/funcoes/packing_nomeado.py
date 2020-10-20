# **kwargs
def resultado_f1(**podium):  # aqui empacota
    print(type(podium))
    for posicao, piloto in podium.items():  # loop no pacote
        print(f'{posicao} -> {piloto}')


if __name__ == '__main__':
    resultado_f1(primeiro='L.Hamilton',
                 segundo='M. Vestappen', terceiro='S.Vettel')
