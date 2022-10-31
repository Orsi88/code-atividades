#Gerar uma matriz (5X5) com o valor 0.

from numpy import array

m = array([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

for l in range(0, 5):
    for c in range(0, 5):
        print(m[l, c], end=' ')
    print()