#Crie um gráfico de dispersão com o intervalo de 0 a 4 para o eixo x e no eixo y, com 0.2 de intervalo nos dois eixos.

from numpy import *
from matplotlib.pyplot import *
from random import randint
x = arange(0, 4, 0.2)
y = arange(0, 4, 0.2)
for indice in range(y.shape[0]):
 y[indice] = y[indice] + randint(-1, 1)
scatter(x, y) 
show() 