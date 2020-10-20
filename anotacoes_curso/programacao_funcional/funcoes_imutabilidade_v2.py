from functools import reduce
from operator import add

valores = (30, 10, 25, 70, 100, 94)


# Não alteram a lista
print(sorted(valores))  # procedural
print(valores)
print(min(valores))
print(max(valores))
print(sum(valores))
print(reduce(add, valores))
print(reversed(valores))
print(tuple(reversed(valores)))
print(valores)

# Preferência para imutável
# strings e tuplas são imutáveis
