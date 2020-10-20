
# PEP usar palavra maiúscula para constantes no python
PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')

textos = [
    'João gosta de futebol e política',
    'A praia foi divertida',
    'Tudo bem!'
]

for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui pelo menos uma palavra proibida:', palavra)
            found = True
            break
    if not found:
        print('Texto autorizado:', texto)

    print('++++')

# O break interrompe o for interno mas não o externo.
