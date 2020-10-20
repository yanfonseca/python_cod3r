# shebang

from datetime import datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):  # conceito ducktype
        return self.tarefas.__iter__()

    def add(self, descricao, vencimento=None):  # cria tarefa
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
        return f'{self.descricao}' + ' '.join(status)


class TarefaRecorrente(Tarefa):
    def __init__(self, descricao, vencimento, dias=7):
        # chamando o constrututor da classe 'pai'
        super().__init__(descricao, vencimento)
        # Tarefa.__init__(self, descricao, vencimento) #alternativa para inicializar o construtor
        self.dias = dias

    def concluir(self):
        # redefinição da função concluir, foi o escolhido o mesmo nome
        # porque faz sentido no projeto, mas não é obrigatório
        super().concluir()
        # Tarefa.concluir(self) #alternativa chamar o concluir
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        # conclui a tarefa e ja marca quando será a próxima
        return TarefaRecorrente(self.descricao, novo_vencimento, self.dias)


def main():
    casa = Projeto('Tarefas de Casa')
    casa.add('Passar roupa', datetime.now())  # -timeselta(seconds=10))
    casa.add('Lavar prato')
    # criando tarefa recorrente
    casa.tarefas.append(TarefaRecorrente('Trocar lençóis', datetime.now(), 7))
    casa.tarefas.append(casa.procurar('Trocar lençóis').concluir())
    print(casa)
    print('#####')

    casa.procurar('Lavar prato').concluir()
    for tarefa in casa:
        print(f'-{tarefa}')

    print('#####')
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
