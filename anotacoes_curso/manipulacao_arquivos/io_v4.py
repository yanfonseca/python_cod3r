# !/usr/local/bin/python3

# Acesso por streaming
arquivo = open('dados.csv', encoding='utf-8-sig')

for registro in arquivo:
    # print(registro.split(','))
    # se existir um erro nesse espaço o arquivo não será fechado,
    # por isso, é uma boa prática usar o bloco try/finally
    print('nome: {}, idade: {}'.format(*registro.strip().split(',')))
arquivo.close()  # fechar depois de percorrer o arquivo
