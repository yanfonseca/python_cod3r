# !/usr/local/bin/python3
# Acesso por streaming
# Bloco if sempre fecha o arquivo e conexão, é excelente para evitar erros
# Mesmo que ocorram erros dentro do with o arquivo será fechado
try:
    with open('dados.csv', encoding='utf-8-sig') as arquivo:
        for registro in arquivo:
            print('nome: {}, idade: {}'.format(*registro.strip().split(',')))
except IndexError:
    pass

finally:
    if arquivo.closed:
        print('Arquivo ja foi fechado')
