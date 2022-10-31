#Usando o a classe numpy, imprima a matriz bidirecional  a seguir:

# 2  3  15  6
# 7  4  14  9
# 5  8  12  1

from numpy import array

m = array([[2, 3, 15, 6], [7, 4, 14, 9], [5, 8, 12, 1]])

m[1, 2] = 16
m[0, 1] = 0

for l in range(0, 3):
    for c in range(0, 4):
        print(f'{m[l, c]:^4}', end=' ')
    print()

print()
print(m.max())
print(m.min())
print(m.sum())
cont = 0
for i in range(len(m)):
    cont += 1
print(f'{m.sum() / cont:.2f}')