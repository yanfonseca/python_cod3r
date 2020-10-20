a = [1, 2, 3, 4]

b = a.pop()

c = a

c.pop()


print(a == c)
print(a, 'id(a) = ', id(a))
print(b, 'id(b) = ', id(b))
print(c, 'id(c) = ', id(c))


a = "string"

b = a

c = b

b.upper()

print(a == c)
print(a, 'id(a)', id(a))
print(b, 'id(b)', id(b))
print(c, 'id(c)', id(c))

a = {'nome': 'y', 'sobrenome': 'f'}

b = a
b.popitem()

c = b

d = c.copy()


print(a == c)
print(a, 'id(a)', id(a))
print(b, 'id(b)', id(b))
print(c, 'id(c)', id(c))
print(d, 'id(d)', id(d))
