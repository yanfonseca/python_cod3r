dicionario = {i: i * 2 for i in range(10) if i % 2 == 0}
print(type(dicionario))
print(dicionario)

dicionario = {f'Item {i}': i * 2 for i in range(10) if i % 2 == 0}
print(dicionario)
