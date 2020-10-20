from pacote1.modulo1 import soma
from pacote2.modulo1 import subtracao
from pacote2.pacote3.modulo1 import soma as soma_pacote3  # igual a soma

# acessando a funcao diretamente

print('soma', soma(3, 2))
print('subtracao', subtracao(3, 2))
print('soma através do pacote3', soma_pacote3(3, 2))

# fachada == façade
# padrão de projeto
# principais produtos
