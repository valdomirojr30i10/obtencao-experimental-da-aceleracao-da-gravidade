
# Le um arquivo com 5 valores de tempo para cada experimento, e insere cada 
# linha em uma lista de tipo float. Retorna a lista caso o arquivo exista ou
# retorna 0 caso ocorra erro ao abrir o arquivo
def ler_arquivo(arq):
    arquivo = open(arq,"r")
    if(arquivo):
        l = []
        for i in range(5):
            l.append(float(arquivo.readline()))
        arquivo.close()
        return l 
    else:
        print("falha ao abrir arquivo!")
        return 0

#efetua leitura dos arquivos de valores experimentais
def recebe_tempos():
    tempos = []
    tempos.append(ler_arquivo("0.84m.txt"))
    tempos.append(ler_arquivo("1.05m.txt"))
    tempos.append(ler_arquivo("1.24m.txt"))
    tempos.append(ler_arquivo("1.88m.txt"))
    tempos.append(ler_arquivo("2.19m.txt"))
    return tempos
    
#Efetua o calculo da media dos valores de uma lista 
def media(lista):
    if(lista):
        s = 0
        for i in range(len(lista)):
            s = s + lista[i]
        return s/len(lista)
    else:
        return 0
    
#Efetua o calculo de desvio padrão dos valores de uma lista
def desvio_padrao(lista):
    if(lista):
        s = 0
        for i in range(len(lista)):
            s = s + (lista[i]-media(lista))**2 
        s = (s/len(lista))**(1/2)
        return s
    else:
        return 0        
    
#Imprime em um arquivo os valores respectivos de altura, tempo e desvio 
# padrão
def imprime(altura,tempo):
    dados = open("redução_dos_dados_experimentais.txt","w")

    for i in range(len(altura)):
        m = media(tempo[i])
        d = desvio_padrao(tempo[i])
                          
        print("altura: ", altura[i], end =', ')
        print("tempo: {:.2f}s".format(m), end =', ')
        print("desvio padrão: {:.2f}s".format(d))
        dados.write("altura: {}, ".format(altura[i]))
        dados.write("tempo: {:.2f}s, ".format(m))
        dados.write("desvio padrão: {:.2f}s\n".format(d))
    dados.close()   

def main():
    tempos = recebe_tempos()
    alturas = ('0.84m','1.05m','1.24m','1.88m','2.19m')    
    
    imprime(alturas,tempos)

main()