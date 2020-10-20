# !/usr/local/bin/python3

# Acesso por streaming
arquivo = open('dados.csv', encoding='utf-8-sig')

for registro in arquivo:
    # print(registro.split(','))
    print('nome: {}, idade: {}'.format(*registro.strip().split(',')))
arquivo.close()  # fechar depois de percorrer o arquivo
