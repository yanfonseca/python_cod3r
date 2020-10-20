# shebang

from datetime import datetime


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        #print(type((' (Concluída)' if self.feito else '')))
        return self.descricao + (' (Concluída)' if self.feito else '')


def main():
    # lista de objetos do tipo tarefa
    casa = []
    casa.append(Tarefa('Passar roupa'))
    casa.append(Tarefa('Lavar prato'))
    casa.append(Tarefa('Passar roupa'))
    casa.append(Tarefa('Lavar prato'))

    # Desafio - > lavar prato
    [tarefa.concluir() for tarefa in casa if tarefa.descricao == 'Lavar prato']

    for tarefa in casa:
        print(f'- {tarefa}')  # chama o __str__


if __name__ == '__main__':
    main()
