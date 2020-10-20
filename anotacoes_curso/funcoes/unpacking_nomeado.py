# **kwargs
def resultado_f1(primeiro, segundo, terceiro):
    print(type(primeiro))
    print(f'1){primeiro}')
    print(f'2){segundo}')
    print(f'3){terceiro}')


if __name__ == '__main__':
    podium = {'primeiro': 'L.Hamilton',
              'segundo': 'M. Vestappen',
              'terceiro': 'S.Vettel'}
    print(type(podium))
    resultado_f1(*podium)  # keys -> desempacota e passa na sequência
    resultado_f1(**podium)  # values -> desempacota e passa na sequência

# Uma alternativa para resultado_f1 seria empacotar novamente e criar as strings com loop
