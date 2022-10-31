#Crie um gráfico de função linear com o intervalo de 0 a 4 para o eixo x.

from numpy import * 
from matplotlib.pyplot import *
x = arange(0, 4)
print(x)
y= x + 2
print(y)
plot(x, y)
show()