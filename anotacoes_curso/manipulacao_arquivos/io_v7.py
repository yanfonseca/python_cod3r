# !/usr/local/bin/python3
# Acesso por streaming
# Bloco if sempre fecha o arquivo e conexão, é excelente para evitar erros
try:
    with open('dados.csv', encoding='utf-8-sig') as arquivo:
        with open('pessoas.txt', 'w', encoding='utf-8-sig') as saida:
            for registro in arquivo:
                pessoa = registro.strip().split(',')
                print('nome: {}, idade: {}'.format(*pessoa), file=saida)

except IndexError:
    pass

finally:
    if arquivo.closed:
        print('Arquivo ja foi fechado')
    if saida.closed:
        print('Arquivo ja foi fechado')
