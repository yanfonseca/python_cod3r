bloco_atrs = ('bloco_accesskey', 'bloco_id')
ul_atrs = ('ul_id', 'ul_style')


def tag_bloco(conteudo, *args, classe='success', inline=False, **novos_atrs):
    tag = 'span' if inline else 'div'

    # informa args e novos_atrs - os dois empacotados para o tag_lista que é igual a conteudo
    # informa os pacotes e a constante bloco_atrs
    html = conteudo if not callable(
        conteudo) else conteudo(*args, **novos_atrs)

    atributos = filtrar_atrs(novos_atrs, bloco_atrs)
    return f'<{tag} {atributos} class = "{classe}">{html}</{tag}>'


def tag_lista(*itens, **novos_atrs):
    # contatena as strings com o texto ''. É uma forma de evitar soma de strings
    lista = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul {filtrar_atrs(novos_atrs,ul_atrs)}>{lista}</ul>'


# recebe empacotado para fazer o loop. Split para pegar a classe
def filtrar_atrs(informados, suportados):
    return ' '.join(f'{k.split("_")[-1]}="{v}"' for k, v in informados.items() if k in suportados)


if __name__ == '__main__':

    print(tag_bloco('bloco'))

    # Por conta dos * args e ** kwargs é necessário passar parametros com nomes
    print(tag_bloco('Inline e classe', classe='info', inline=True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco(inline=True, conteudo='inline'))
    print(tag_bloco('falhou', classe='error'))

    # # Duas funções, usando o tag_lista
    # Só informa args para tag_lista
    print(tag_bloco(tag_lista('item 1', 'item 2'), classe='info'))

    # Informa a função tag_lista
    print(tag_bloco(tag_lista, 'Sabado', 'Domingo',
                    classe='info', inline=True))  # Não entra filtrar_atrs

    print(tag_bloco(tag_lista, 'item 1', 'item 2', classe='info',
                    bloco_accesskey='m', bloco_id='conteudo', ul_id='lista', ul_style='color:red'))
