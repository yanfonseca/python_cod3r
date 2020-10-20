def tag_bloco(texto: str, classe: str = 'success') -> str:
    return f'<div class = "{classe}">{texto}</div>'


if __name__ == '__main__':
     # Testes (assertions) - Isso não é teste unitário
    assert tag_bloco('Incluído com sucesso!') == \
        '<div class = "success">Incluído com sucesso!</div>'
    assert tag_bloco('Impossível excluir!', 'error') == \
        '<div class = "error">Impossível excluir!</div>'
    print(tag_bloco('bloco'))
    print(tag_bloco('bloco', 'erro'))
