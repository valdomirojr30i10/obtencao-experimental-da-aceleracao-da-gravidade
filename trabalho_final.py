import ajuste
import tratar_dados
import plot_errobar_dados as plot
import numpy as np

dados = tratar_dados.tratar_dados("redução_dos_dados_experimentais.txt")
alturas, tempos, desvios = dados


# Com o ajuste da função "t = (2*h/g)**(1/2)", foram obtidos:
# Y = ln(t**2)  
# x = ln(h)
# a0 = ln(2)-ln(g)
# a1 = 1

Y = [np.log(i**2) for i in tempos]
x = [np.log(i) for i in alturas]

a0,a1 = ajuste.reta(x,Y)
g = 2/np.e**a0

print("a1 teorico: 1. a1 encontrado: ",a1)
print("g encontrado: ", g)

plot.plotagem(dados,g)
