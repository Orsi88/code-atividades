#Crie um gráfico de função exponencial com o intervalo de 0 a 4 para o eixo x, com 0.2 de intervalo.

from numpy import *
from matplotlib.pyplot import *
x = arange(0, 4, 0.2)
print(x)
y = 3**x
print(y)
plot(x, y)
show()