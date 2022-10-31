x = {'a', 'b', 'c', 'd', 'e'}
y = {'d', 'e', 'f', 'g'}
z = {'a', 'b'}

x.union(y)
x.intersection(y)
x.intersection_update(y)
x.difference(y)
x.symmetric_difference(y)
print('e' and 'f' in x)
print(z.issubset(x))
print(z.issuperset(x))
print(x.isdisjoint(y))


