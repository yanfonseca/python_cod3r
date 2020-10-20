def log(function):
    def decorator(*args, **kwargs):
        return function(*args, **kwargs)
    return decorator


@log
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
    print('>', sub(5, 7))
    print('###')
