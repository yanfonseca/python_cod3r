# Python 3  
    Anotações, observações e desafios do Curso Python 3 - Cod3r

    Revisado até 11.Funções

    O que são collections?
        
        https://www.caelum.com.br/apostila-python-orientacao-a-objetos

## Filosofia

    Zen of Python
    * import this
    
    PEP 8 - Procurar sobre PEPs

## Visual Studio Code

É possível criar células como de um jupyter notebook usando "# %%", eessa forma, é possível programar em um arquivo ".py".

## Observações

    A tupla é imutável.

    Use letras maiúsculas para representar constantes.
    
    Use a função dir() para inspecionar as possibilidades ações das funções.
    
    Sempre use a estrutura: "if __name__ == '__main__':" 

    Para alterar o último caractere da função print.
        print('texto', end=',')
        print('texto, end-'\n')

    Controle dentro de loop:
        pass: Evita que o programa seja interrompido mas não altera o contador.
        continue: Não interrompe o programa e soma 1 ao contador.
        break: Interrompe o loop.

    Nunca usar atributo mutável(use tuplas) como valor padrão de uma função. Isso evita problemas com os valores padrões passados para funções. Se for usado tipo mutável a referência para a memória não é alterada e isso gera resultados inesperados.
    
    Reuso de código:
    
    HERANÇA(OO) VS COMPOSIÇÃO
        Priorizar composição usando decorator.

    Dentro de um pacote(pasta) tem que existir o arquivo __init__.py para o python entenda que se trata de um pacote.

    Usar a estrutura façade(fachada) para tornar mótulos acessíveis.


## Paradigma da Orientação ao Objeto - OO

    Normalmente é usado o paradigma procedural, o qual tem foco no algoritmo, na função. => funcao(dado)
    
    Para OO o foco é no dado -> dado.funcao() -> objeto.metodo
    
    Com OO é possível retratar de maneira mais fácil cenários do mundo real em forma de código
        Um bjeto é formado por (atributos e comportamentos) ou (dados e métodos) ou (atributos e métodos) que são instânciados em uma classe.

### Classe vs Objeto
    A classer cria o molde de algo e objeto é a instância desse molde.
        classe == molde
        objeto == instância

### Pilares da OO

    Herança (simples e múltipla)
        Classe carro:
        Abstraindo...
            civic é um carro. Então é herda, assim é o paradigma de OO. Foco no objeto.
            carro tem um motor. É uma composicao. Foco na função.
            Os herdeiros de uma classe também são do mesmo tipo da class pai.   

    Polimorfismo
        Capacidade de substituir um elemento concreto por um elemento abstrato.
            duck typing

    Encapsulamento
        Capacidade de usar determinado objeto sem entender a parte interna do mesmo, o usuário não precisa saber como a classe e método é construído. Basta saber interagir com a classe, é suficiente.
        objeto é uma capsula, agrupa membros(dados e comportamentos)
    
    Abstração
        Usar o mundo real para a criação do software através de uma simplificação, abstração.

            class HOSPITAL
                cliente
                - tipo sanguineo
                - n carteira

            class MECANICO
                cliente
                - tipo de carro
                - placa

### Convensão - métodos privados
    Todos os métodos são acessíveis públicos, diferente de outras linguagens.
    
    Existe uma convenção na qual diz que funções iniciadas por 'underscore' não devem ser acessadas diretamente e são considerados métodos privados.
        def _metodo():
 
    No python não existe mais de um construtor.
    
    Python nao suporta sobrecarga de métodos(métodos com mesmo nome)

    Simulução de overload
        Para simular é possível ter um método que recebe outros métodos considerados privados.

            def _add1(args):
                pass
            
            def _add2(args):
                pass
            def _add(args):
                _add1(args)
                _add2(args)
                pass

    Sobrecarrega de operadores
    Exemplos:

        [1, 2, 3] + [4, 5, 6] ==[1, 2, 3, 4, 5, 6]
        set3 = se1 - set2 

    É possível alterar operadores acessando os métodos dentro de uma classe, por exemplo:
    __def __iadd__(): #operador +=


    funcao sorted()
    

Membros Instância vs Estáticos
    instanciar objetos
    instancia - posso passar o valor

    instancia e objeto sao sinônimos
    d1 = Data(...)
    d1.dia = 10

    estáticos - pode ser acessado diretamente da classe
    compartilhados com todos objetos
    valor da classe

    Data.ano = 2020

    método de classe vs método estático
    classe
    d1 = Data(...)
    d1.metodo()

    metodo estatico
    Data.metodo_estatico()

        # metodo de instancia, metodo de classe e metodo estático
    # metodo de instancia recebe instancia(self)
    # metodo de classe recebe o atributo de classe
    # metodo estatico nao recebe nao parametro

    classe abstrata nao é nativa do python x concreta
    

    python aceita herança múltipla


https://www.w3schools.com/python/ref_func_isinstance.asp


site bom - https://www.python-course.eu/python3_decorators.php

x = isinstance(5, int)

### Repositório Cod3r 
        https://github.com/cod3rcursos/curso-python



pip install -r requirements.txt

python -m site

pip list --outdated