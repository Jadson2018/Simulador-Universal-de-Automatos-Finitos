#Código desenvolvido pelo aluno Aluno Jadson Costa de Amorim
#função criada para a variável do número de cadeias
def edez(c):
    if(int(c)<=10):
        return int(c)
    else:
       return -1
def main():
    #a leitura dos arquivos é feita linha por linha
    numerodeestados = input(" ")
    simbolosterminais = input(" ")
    nestadosiniciais = input(" ")
    estadosdeaceitacao = input(" ")
    ntransicoes = input(" ")
    transicoes=[]
    cadeias=[]
    #a partir da quarta linha não se sabe quantas existirão então é feito um laço somando 5 linhas
    cont = 0
    while(cont<int(ntransicoes)):
         dado=input(" ")
         transicoes.append(dado)
         cont = cont+1
    dadotemporario = input(" ")
    ncadeias = edez(dadotemporario)
    if(ncadeias==-1):
        print(">>>limite de cadeias atingido")
        exit()

    cont = cont+4+2
    cont2 = 0
    #mais um laço é feito somando com o resultado de todas as linhas até a atual
    while(cont2<ncadeias):
        dado2=input(" ")
        cadeias.append(dado2)
        cont2 = cont2+1
    interpretador(numerodeestados,simbolosterminais,nestadosiniciais,estadosdeaceitacao,ntransicoes,transicoes,ncadeias,cadeias)
def pertenceAoAlfabeto(alfabeto,simbolo):
    #o numero de simbolos finais do alfabeto é lido pegando o primeiro caractere da linha correspondente
    numero = int(alfabeto[0])
    i = 0
    boolean = 0
    while(i<numero):
        #o loop é incrementado de dois em dois lendo a partir do segunda caractere
        if(alfabeto[2+2*i]==simbolo):
            boolean = 1
        i = i+1
    return boolean
#essa função procura pelo início do automato verificando se o primeiro simbolo da cadeia se inicia em um estado menor que a quantidade de estados iniciais de acordo com as transicoes
def setInicio(estadosiniciais,ntransicoes,transicoes,simbolo):
    i = 0
    inicio = 0
    if(int(estadosiniciais)==1):
       inicio = 0
    else:
        while(i<int(ntransicoes)):
            transicao = transicoes[i]
            if(transicao[2]==simbolo):
                if(int(transicao[0])<int(estadosiniciais)):
                    inicio = int(transicao[0])
                else:
                    inicio = -1
            i=i+1
    return inicio
#essa função verifica o estado atual e a transicao atual(simbolo) se eles estiverem na lista de transicoes o estado atual passa a ser o próximo onde a próxima transiçao começará
def setProximoEstado(transicao,estado,ntransicoes,listatransicoes):
    i = 0
    encontrou = 0
    while(i<int(ntransicoes)):
       transicoes = listatransicoes[i]
       if(int(transicoes[0])==estado and transicoes[2]==transicao):
              encontrou = 1
              proximoestado = int(transicoes[4])
              break
       i=i+1
    if(encontrou==1):
        return proximoestado
    else:
        return -1
#determina se o estado atual é um estado final
def efinal(EstadoAtual,estadosfinais):
    i = 0
    eFinal = 0
    while(i<int(estadosfinais[0])):
        if(EstadoAtual==int(estadosfinais[2+2*i])):
            eFinal = 1
        i=i+1
    return eFinal
#escreve no arquivo saida se as cadeias pertencem ou não a linguagem lida
def Saida(aceitacao):
    if(aceitacao==1):
       print("aceita\n")
    else:
        print("rejeita\n")
def interpretador(numerodeestados,simbolosterminais,nestadosiniciais,estadosdeaceitacao,ntransicoes,transicoes,ncadeias,cadeias):
    #o primeiro loop percorre a lista de todas as cadeias
    cont=0
    while(cont<ncadeias):
        cadeiaAtual = cadeias[cont]
        cont2 = 0
        #a variavel pertence diz se a cadeia pertence ou não a linguagem
        pertence = 1
        EstadoAtual = setInicio(nestadosiniciais,ntransicoes,transicoes,cadeiaAtual[0])
        tamanhocadeia = len(cadeiaAtual)
        #o segundo loop percorre a string da cadeia atual
        while(cont2<tamanhocadeia):
            #primeiro é verificado se o caractere lido pertence a cadeia
            if(pertenceAoAlfabeto(simbolosterminais,cadeiaAtual[cont2])==1):
                #caso pertença é verificado se o existe transição
                EstadoTemporario = setProximoEstado(cadeiaAtual[cont2],EstadoAtual,ntransicoes,transicoes)
                if(EstadoTemporario==-1):
                    pertence = 0
                    cont2 = cont2+1
                else:
                    #caso exista é verificado se o simbolo vazio é o atual
                    if(cadeiaAtual[cont2]=="-"):
                        #se for verifica se ele o estado atual é final, por que ele só pode ser aceito em estados finais
                        if(efinal(EstadoAtual,estadosdeaceitacao)==1):
                           cont2 = cont2+1
                        else:
                            pertence = 0
                            cont2=cont2+1
                    else:
                        #caso não seja é verificado se o simbolo é o último da cadeia
                       if(cont2<tamanhocadeia-1):
                          #caso não seja o próximo estado é setado no estado atual
                          EstadoAtual = EstadoTemporario
                          cont2 = cont2+1
                       else:
                           #caso seja é setado o próximo estado e verificado se ele é final
                           EstadoAtual = EstadoTemporario
                           if(efinal(EstadoAtual,estadosdeaceitacao)==0):
                            #se não for a cadeia não pertence a linguagem
                              pertence = 0
                           cont2 = cont2+1
                            
            else:
                pertence = 0
                cont2=cont2+1
        Saida(pertence)
        cont = cont+1
#main é chamada para iniciar o programa
main()
          
