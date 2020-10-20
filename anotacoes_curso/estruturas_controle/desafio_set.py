# PEP usar palavra maiúscula para constantes no python
PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'política'}

textos = [
    'João gosta de futebol e política',
    'A praia foi divertida',
    'Tudo bem!'
]

for texto in textos:

    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))

    print(
        f'Possui palavras proibidas: {intersecao}' if intersecao else f'Texto autorizado: {texto}'
    )
