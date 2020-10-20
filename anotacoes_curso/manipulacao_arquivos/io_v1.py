# !/usr/local/bin/python3

arquivo = open('dados.csv', encoding='utf-8-sig')

dados = arquivo.read()  # carrega o arquivo completamente
arquivo.close()
print(dados.splitlines())
print(dados.splitlines()[0].split(','))

for registro in dados.splitlines():
    # print(registro.split(','))
    # Informando uma lista, por isso o asterisco desempacota em sequência para
    # alimentar a função format.
    print('nome: {}, idade: {}'.format(*registro.split(',')))

    # alternativa
    # print('nome: {}, idade: {}'.format(
    #     registro.split(',')[0], registro.split(',')[1]))
