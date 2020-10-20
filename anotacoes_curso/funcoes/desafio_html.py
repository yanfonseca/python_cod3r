def tag(tag, *args, **kwargs):
    if 'html_class' in kwargs:
        print(dict(kwargs))
        # pop retorna o valor da key html_class.
        # É adicionado em class que é um nome padrão do python e por isso não foi utilizado
        kwargs['class'] = kwargs.pop('html_class')
        print(dict(kwargs))

    attrs = ''.join(f'{k}="{v}"' for k, v in kwargs.items())
    inner = ''.join(args)
    return f'<{tag} {attrs}>{inner}</{tag}>'


if __name__ == '__main__':
    print(tag('p',
              tag('span', 'Curso de Python 3, por '),
              tag('strong', 'Juracy Filho', id='jf'),
              tag('span', '.'),
              html_class='alert'
              )
          )
