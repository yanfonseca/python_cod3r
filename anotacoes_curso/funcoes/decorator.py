# decorator - possibilidade de fazer uma ação antes e depois,
# intercepta a função e modifica e depois retorna o resultado para a função
# função interna que vai ser decorada, log vai ser o decorator


def log(function):  # function é decorada
    def decorator(*args, **kwargs):  # foi criada para receber qualquer argumentos
        print(f'Início da chamada da função: {function.__name__}')
        print(f'args: {args}')  # posicionais
        print(f'kwargs: {kwargs}')  # nomeados
        resultado = function(*args, **kwargs)
        print(f'Resultado da chamada: {resultado}')
        return resultado
    return decorator


@log  # A função soma é decorada e a função log decora a funcao soma e a retorna
def soma(x, y):
    return x + y


@log
def sub(x, y):
    return x - y


if __name__ == '__main__':
    print('>', soma(5, 7))
    print('###')
    print('>', soma(5, y=7))
    print('###')
    print('>', soma(x=5, y=7))
    print('###')
    print('>', sub(5, 7))
    print('###')

    # print('>', sub(x=5, 7))
    # Isso vai mostrar um erro porque keyword argument está
    # antes de um positional argument
    # print('###')
