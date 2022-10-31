#Crie um gráfico de função logarítmica com o intervalo de 0 a 4 para o eixo x, com 0.2 de intervalo.

from numpy import *
from matplotlib.pyplot import *
x = arange(0, 4, 0.2)
print(x)
y = log(x)
print(y)
plot(x, y)
show()