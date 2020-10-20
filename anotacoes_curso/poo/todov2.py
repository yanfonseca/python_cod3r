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


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def add(self, descricao):
        self.tarefas.append(Tarefa(descricao))

    def pendentes(self):  # busca feito usando a classe tarefa
        # .feito acessa classe tarefa
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):  # busca a descricao usando a classe tarefa
        # possível index error
        return [tarefa for tarefa in self.tarefas
                if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefas(s) pendentes(s))'


def main():
    casa = Projeto('Tarefas de Casa')
    casa.add('Passar roupa')
    casa.add('Lavar prato')
    print(casa)  # print(__str__) associado a classe projeto

    casa.procurar('Lavar prato').concluir()
    for tarefa in casa.tarefas:
        print(f'-{tarefa}')  # print(__str__) associado a classe tarefa

    print(casa)

    mercado = Projeto('Compras do mercado')
    mercado.add('Frutas secas')
    mercado.add('Carne')
    mercado.add('Tomate')
    print(mercado)

    mercado.procurar('Carne').concluir()
    for tarefa in mercado.tarefas:
        print(f'-{tarefa}')


if __name__ == '__main__':
    main()
