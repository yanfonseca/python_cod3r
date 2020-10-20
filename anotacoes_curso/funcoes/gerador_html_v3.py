def tag_bloco(conteudo: str, classe: str = 'success', inline=False) -> str:
    tag = 'span' if inline else 'div'
    return f'<{tag} class = "{classe}">{conteudo}</{tag}>'


def tag_lista(*itens):
    # contatena as strings com o texto ''. É uma forma de evitar soma de strings com +
    # desempacotado
    lista = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':

    print(tag_bloco('bloco'))
    print(tag_bloco('Inline e classe', 'info', True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco(inline=True, conteudo='inline'))
    print(tag_bloco('falhou', classe='error'))

    # Duas funções
    # Alterando o conteúdo
    print(tag_bloco(tag_lista('item 1', 'item 2'), classe='info'))
