#Cria listas com os valores de altura, tempo e desvio padrão atraves dos
#dados obtidos no programa 'redução de dados experimentais'
def tratar_dados(arq):
    #abre arquivo no modo leitura
    dados = open(arq,"r")
    if(dados):
        a = []
        t = []
        d = [] 
        
        #atribui para as listas alturas, tempos e desvios, os valores adquiridos
        # pelo programa 'reducao_dados_experimentais.py'
        for i in range(5):
            #adiciona uma linha do arquivo a cada iteração dentro de uma string 
            #chamada 'linha'
            linha = dados.readline()
            
            #remove strings de altura, tempo e desvio. Deixando assim, somente
            #os valores reais com suas unidades de medida
            linha = linha.replace("altura: ", "")
            linha = linha.replace(", tempo: ", "")
            linha = linha.replace(", desvio padrão: ", "")
            
            #localiza valores de altura, tempo e desvio padrão com base nas
            #unidades de medida, efetua o corte da string, e insere esses 
            #valores dentro de suas respectivas listas
            a.append(linha[0:linha.find('m')])
            t.append(linha[linha.find('m')+1:linha.find('s')])
            d.append(linha[linha.find('s')+1:-2])
       
        dados.close()   
            
        #Converte as listas para o tipo float
        a =  [float(i) for i in a]
        t =  [float(i) for i in t]
        d =  [float(i) for i in d]
        
        lista = [a,t,d]
        
        return lista
    else:
        print("falha ao abrir o arquivo")
        return 0