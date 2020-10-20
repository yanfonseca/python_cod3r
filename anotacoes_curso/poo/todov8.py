# shebang

from datetime import datetime, timedelta


class TarefaNaoEncontrada(Exception):
    pass


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):  # conceito ducktype
        return self.tarefas.__iter__()

    # https://docs.python.org/3/library/operator.html
    # sobrecarga do operador +=
    # projeto += tarefa
    # casa += ...
    def __iadd__(self, tarefa):
        tarefa.dono = self
        self._add_tarefa(tarefa)
        return self

    def _add_tarefa(self, tarefa, **kwargs):  # método privado, convenção
        self.tarefas.append(tarefa)

    # método privado, convenção - vencimento estará em kwargs
    def _add_nova_tarefa(self, descricao, **kwargs):
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento', None)))

    # isinstance(parametro, class) confere o tipo da classe parametro
    def add(self, tarefa, vencimento=None, **kwargs):
        funcao_escolhida = self._add_tarefa if isinstance(tarefa, Tarefa) \
            else self._add_nova_tarefa
        kwargs['vencimento'] = vencimento

        # os métodos _add_tarefa e _add_nova_tarefa tem os mesmos parametros para facilitar a chamada com funcao_escolhida()
        funcao_escolhida(tarefa, **kwargs)

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        # possível IndexErro
        try:
            return [tarefa for tarefa in self.tarefas
                    if tarefa.descricao == descricao][0]
        except IndexError as e:
            # podia usar somente Expection, de forma generica "except Expection as e"
            # se fosse passado outra exception except RuntimeError as e: a exception não é tratada então o código é travado
            # return None também gera problema, porque uma funcao pode tentar excecutar o que é nulo
            raise TarefaNaoEncontrada(str(e))

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
        super().__init__(descricao, vencimento)
        self.dias = dias
        self.dono = None

    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        nova_tarefa = TarefaRecorrente(
            self.descricao, novo_vencimento, self.dias)
        if self.dono:
            self.dono += nova_tarefa
        return nova_tarefa


def main():
    casa = Projeto('Tarefas de Casa')
    casa.add('Passar roupa', datetime.now())  # -timeselta(seconds=10))
    # casa.add('Lavar prato')
    casa += Tarefa('Lavar prato')
    casa += TarefaRecorrente('Trocar lençóis', datetime.now(), 7)
    casa.procurar('Trocar lençóis').concluir()
    print(casa)

    try:
        casa.procurar('Lavar prato - ERRO').concluir()
    except TarefaNaoEncontrada as e:
        print(f'A causa foi "{e}"!')
    finally:
        print('Sempre será executado!')

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
