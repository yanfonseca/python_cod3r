def tag_bloco(texto: str, classe: str = 'success', inline=False) -> str:
    # com o inline é escolhdida a tag
    tag = 'span' if inline else 'div'
    return f'<{tag} class = "{classe}">{texto}</{tag}>'


if __name__ == '__main__':

    print(tag_bloco('bloco'))
    print(tag_bloco('Inline e classe', 'info', True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco(inline=True, texto='inline'))
    print(tag_bloco('falhou', classe='error'))
