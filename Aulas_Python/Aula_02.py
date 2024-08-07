# Aula 02 - Introdução ao Python: Bibliotecas e Virtualenv
# Instala as bibliotecas: pip install numpy matplotlib
import numpy as np
from matplotlib import pyplot as plt

f = 60 #Frequência
T = 1/f #periodo
A =  220 * np.sqrt(2) #amplitude
t = np.arange(0,2*T,T/200)
y = A * np.sin(2*np.pi*f*t)

plt.title("Demonstração Matplotlib")
plt.xlabel("Tempo [s]")
plt.ylabel("Tensão [V]")
plt.plot(t,y)
plt.show()
