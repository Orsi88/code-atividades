#Crie um gráfico de função coseno com o intervalo de 0 a 4 para o eixo x, com 0.4 de intervalo

from numpy import *
from matplotlib.pyplot import *
x = arange(0, 4, 0.4)
print(x)
y = sin(x)
print(y)
plot(x, y)
show()