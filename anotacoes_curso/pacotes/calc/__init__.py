from pacote1.modulo1 import soma
from pacote2.modulo1 import subtracao


__all__ = ['soma', 'subtracao']

# pacote façade
# a partir de calc é possível acessar outros módulos
# __all__ com todas as funcionalidades que eu quero exportar
# fachada == façade
# padrão de projeto
# principais produtos
