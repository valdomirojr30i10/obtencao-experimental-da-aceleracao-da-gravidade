import matplotlib.pyplot as plt

def plotagem(lista,g_experimental): 
    if(lista):
        g = 8.81
        h = []
        # Essa seção gera pontos para h
        inicio = 0.6
        fim    = 2.5
        qtde_pontos = 20
        percorre = inicio
        for i in range(qtde_pontos):
            h.append(percorre)
            # print(percorre)
            percorre += (fim-inicio)/(qtde_pontos-1)
            
        
        # 'y = (2*h/g)**(1/2)' em pontos de h:
        y = [((2*i)/g)**(1/2) for i in h]
        y_experimental = [(2*i/g_experimental)**(1/2) for i in h]
    
        plt.plot(h, y, label='g = 9.81 m/s²')
        plt.xlabel('Altura (m)')
        plt.ylabel('Tempo (s)')
        plt.suptitle("Grafico Altura X Tempo de queda", fontsize=18)
        plt.plot(h,y_experimental, label='g = {:.2f}m/s²'.format(g_experimental))
        plt.legend(loc=2)
        plt.errorbar(lista[0],lista[1], yerr = lista[2], fmt = 'ro',)
        plt.axis([inicio, fim, 0.35, 0.75])   
        plt.grid(True)  
        plt.show()
        
    else:
        print("nenhuma lista foi recebida")
