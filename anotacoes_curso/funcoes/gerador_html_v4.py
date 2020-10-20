# depois de *pack tem que usar todos argumentos posicionais
# na chamada da função em todos parametros depois de *args


def tag_bloco(conteudo: str, *args, classe: str = 'success', inline=False) -> str:
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args)
    return f'<{tag} class = "{classe}">{html}</{tag}>'


def tag_lista(*itens):
    # Asterisco dentro da função é empacotamento dos dados em uma tupla
    # contatena as strings com o texto ''. É uma forma de evitar soma de strings
    lista = (f'<li>{item}</li>' for item in itens)
    # print(lista) - no caso é um generator
    # O join pode receber lista ou generator para fazer a concatenção. Não há diferença!
    lista = ''.join(lista)
    # print('tipo', type(lista)) # Retorna string
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':

    print(tag_bloco('bloco'))
    print(tag_bloco('Inline e classe', classe='info', inline=True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco(inline=True, conteudo='inline'))
    print(tag_bloco('falhou', classe='error'))
    print(tag_bloco(tag_lista('item 1', 'item 2'), classe='info'))
    print(tag_bloco(tag_lista, 'Sabado', 'Domingo',
                    classe='info', inline=True))  # depois de pack tem que usar todos argumentos posicionais
