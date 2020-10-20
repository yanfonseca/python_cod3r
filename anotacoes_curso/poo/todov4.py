# shebang

from datetime import datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):  # conceito ducktype
        return self.tarefas.__iter__()

    def add(self, descricao, vencimento=None):
        self.tarefas.append(Tarefa(descricao, vencimento))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        # possível index error
        return [tarefa for tarefa in self.tarefas
                if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefas(s) pendentes(s))'


class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            status.append('(Concluída)')
        elif self.vencimento:  # se for diferente de None
            if datetime.now() > self.vencimento:
                status.append('(Vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(Vence em {dias} dias)')
        else:
            status.append('(Falta informação)')
        # é usado o ' '.join pois é uma maneira mais simples de concaternar comparado array[posicao]. O join itera em objeto iterável
        return f'{self.descricao}' + ' '.join(status)
        # return f'{self.descricao}' + status[0]


def main():
    # Cada tarefa tem uma descrição e um vencimento
    casa = Projeto('Tarefas de Casa')
    casa.add('Passar roupa', datetime.now())  # -timeselta(seconds=10))
    casa.add('Lavar prato')
    print(casa)

    casa.procurar('Lavar prato').concluir()
    for tarefa in casa:
        print(f'-{tarefa}')

    print(casa)

    mercado = Projeto('Compras do mercado')
    mercado.add('Frutas secas')
    mercado.add('Carne')
    mercado.add('Tomate', datetime.now()+timedelta(days=3, seconds=1))
    print(mercado)

    mercado.procurar('Carne').concluir()
    for tarefa in mercado:
        print(f'-{tarefa}')


if __name__ == '__main__':
    main()
