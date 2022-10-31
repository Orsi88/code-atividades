#Gerar uma matriz (4X4) com o valor 1.

from numpy import array

m = array([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])

for l in range(0, 4):
    for c in range(0, 4):
        print(m[l, c], end=' ')
    print()
