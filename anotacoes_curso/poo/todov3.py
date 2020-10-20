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

    def __iter__(self):  # conceito typing
        return self.tarefas.__iter__()

    def add(self, descricao):
        self.tarefas.append(Tarefa(descricao))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
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
    for tarefa in casa:  # foi adicionado o método def __iter__ e com isso não é necessário casa.tarefas
        print(f'-{tarefa}')  # print(__str__) associado a classe tarefa

    print(casa)

    mercado = Projeto('Compras do mercado')
    mercado.add('Frutas secas')
    mercado.add('Carne')
    mercado.add('Tomate')
    print(mercado)

    mercado.procurar('Carne').concluir()
    for tarefa in mercado:
        print(f'-{tarefa}')


if __name__ == '__main__':
    main()
