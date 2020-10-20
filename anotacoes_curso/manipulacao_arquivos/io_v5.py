# !/usr/local/bin/python3

# Acesso por streaming

try:
    arquivo = open('dados.csv', encoding='utf-8-sig')

    for registro in arquivo:
        print('nome: {}, idade: {}'.format(*registro.strip().split(',')))

except IndexError:
    pass

finally:
    # o bloco finally é executado independente de erro,
    # mas em caso de erro só executa o que está dentro do finnaly e fecha o programa
    # Se existir o except executa o except em caso de erro, vai para o finnaly e continua a rodar o programa.
    print('finally')
    arquivo.close()  # fechar depois de percorrer o arquivo

if arquivo.closed:
    print('Arquivo ja foi fechado')
