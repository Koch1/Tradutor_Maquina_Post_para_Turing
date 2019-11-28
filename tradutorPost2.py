estados={}
estTuring={}
variavel={}
varTuring={0:''}
estadoInicial=0
estadoParada=[]
regras=[]
regrasTuring=[]
estadoAtual=0
palavra=0
import math

def imprimir():
    global estados,estadoInicial,estadoParada, regras
    print("\nEstados: " + str(estados))
    print("\nVariavel: " + str(variavel))
    print("\nEstado Inicial: " + str(estadoInicial))
    print("\nEstados Parada : " + str(estadoParada))
    print("\nEstados Regras : " + str(regras))
    print("\nEstados Regras Turring : " + str(regrasTuring))
    
def imprTuring():
    global estados,estadoInicial,estadoParada,regras,regrasTuring,variavel
    print("Tabela Traducao Estados:")
    for indx, name in enumerate(estados):
      print(str(name)+"|"+estados[name])
    print("Tabela Traducao Variavel:")
    for indx, name in enumerate(variavel):
      print(str(name)+"|"+variavel[name])
    print("Estado Atual | Variavel Lida | Proximo Estado | Simbolo escrito | Movimento")
    for reg in regrasTuring:
      print("("+str(reg[0])+","+str(reg[1])+","+str(reg[2])+","+str(reg[3])+","+str(reg[4])+")")
              
        

def converterd_b(n,elemento):
    binario = ""
    while(True):
        binario = binario + str(n%2)
        n = n//2
        if n == 0:
            break
    binario = binario[::-1]
    elem=int(math.log(elemento)/math.log(2))
    if(((math.log(elemento)/math.log(2))-(elem))>0):
        elem=elem+1
    while True:
        if(len(binario)>=elem):
            break
        else:
            binario=str('0')+binario
    #binario = int(binario)
    #print(binario)
    return binario

#Traduz os estados para binario
def letras():
    global estados,estadoInicial,estadoParada, regras,variavel,regrasTuring
    if(len(estados)>len(variavel)):
        valor=len(estados)
    else:
        valor=len(variavel)
    est={}
    for indx, name in enumerate(estados):
        est['q'+str(converterd_b(name,(len(estados))))]=estados[name]
    estados=est
    var={}
    for indx, name in enumerate(variavel):
        var['a'+str(converterd_b(name,len(variavel)))]=variavel[name]
    variavel=var
    estadoInicial=['q'+str(converterd_b(0,valor))]
    estParada=[]
    for indx, name in enumerate(estadoParada):
        estParada.append('q'+str(converterd_b(name,(len(estados)))))
    estadoParada=estParada
    novaReg=[]
    for indx, name in enumerate(regras):
        regr=[]
        regr.append('q'+str(converterd_b(name[0],(len(estados)))))
        regr.append('a'+str(converterd_b(name[2],len(variavel))))
        regr.append('q'+str(converterd_b(name[3],(len(estados)))))
        novaReg.append(regr)
    regras=novaReg
    novaReg=[]
    for indx, name in enumerate(regrasTuring):
        regr=[]
        regr.append('q'+str(converterd_b(name[0],(len(estados)))))
        regr.append('a'+str(converterd_b(name[1],len(variavel))))
        regr.append('q'+str(converterd_b(name[2],(len(estados)))))
        regr.append('a'+str(converterd_b(name[3],len(variavel))))
        regr.append(name[4])
        novaReg.append(regr)
    regrasTuring=novaReg
        
def leituraArquivo():
    global estados,estadoInicial,estadoParada, regras, estadoAtual,variavel
    bloco = open('teste.txt', 'r')
    #estados=bloco.readline().rstrip("\n\r").split(" ")
    #primeira linha
    estados[len(estados)]=bloco.readline().rstrip("\n\r")
#  #segunda linha,  estados de parada
    #split quebra linha na restrição e strip tira o espaco
    for val in bloco.readline().rstrip("\n\r").split(","):
        v = True
        for est in estados:
            if val.strip()==estados[est]:
                estadoParada.append(est)
                v = False
        if v:
            estados[len(estados)] = val.strip()
            estadoParada.append(len(estados)-1)

#três ou mais leitura das regras
    while True:
        linha=bloco.readline().rstrip("( \n \r )").rstrip("(").replace("(","")
        if(linha.find(',')!=-1):
            reg=linha.split(",")
            if(len(reg)==4):
                v1=True
                v2=True
                # veriffica se tem um estados da regras   ja na lista
                for est in estados:
                    if(reg[0]==estados[est]):
                        reg[0]=est
                        v1=False
                    if(reg[3]==estados[est]):
                        reg[3]=est
                        v2=False
                #adiciona o estado  caso ele n tenha lista
                if(v1):
                    estados[len(estados)]=reg[0].strip()
                    reg[0]=len(estados)-1
                if(v2):
                    estados[len(estados)]=reg[3].strip()
                    reg[3]=len(estados)-1
                v1=True
                for var in variavel:
                    if(reg[2]==variavel[var]):
                        reg[2]=var
                        v1=False
                if(v1):
                    variavel[len(variavel)]=reg[2]
                    reg[2]=len(variavel)-1
            else:
                print("erro  nas regras");
            regras.append(reg)        
        else:
            #para leitura do arquivo
            break
def turing ():
    global estados,estadoInicial,estadoParada,regras,regrasTuring,varTuring,estTuring
    regr=[]
    branco=-1
    varTuring=[]
    for bra in variavel:
      if(variavel[bra]==''):
          branco=bra
      else:
        varTuring.append(bra)
    for regPost in regras:
        if(regPost[1]==''):
            if(regPost[3] in estadoParada):
                regr.append([regPost[0],regPost[2],regPost[3],regPost[2],'f'])
            else:
                regr.append([regPost[0],regPost[2],regPost[3],regPost[2],'d'])
        elif(regPost[1]=='d'):
            if (regPost[3] in estadoParada):
                regr.append([regPost[0],regPost[2],regPost[3],branco,'f'])
            else:
                regr.append([regPost[0],regPost[2],regPost[3],branco,'d'])

        elif(regPost[1]=='i'):
            for var in varTuring:
                regr.append([regPost[0],var,regPost[0],var,'d'])
            novoEst = (len(estados))
            estados[novoEst]="est"+str(novoEst)
            regr.append([regPost[0],branco,novoEst,regPost[2],'e'])
            for var in varTuring:
                regr.append([novoEst,var,novoEst,var,'e'])
            if regPost[3] in estadoParada:
                regr.append([novoEst,branco,regPost[3],branco,'f'])
            else:
                regr.append([novoEst,branco,regPost[3],branco,'d'])
    regrasTuring=regr

def criarArquivosTuring ():
  global estados,estadoInicial,estadoParada,regras,regrasTuring,varTuring,estTuring
  arq = open('resultado.txt', 'w')
  texto = []
  for reg in regrasTuring:
      texto.append("("+str(reg[0])+","+str(reg[1])+","+str(reg[2])+","+str(reg[3])+","+str(reg[4])+")\n")
  arq.writelines(texto)
  arq.close()
  arq = open('tabelaTraducaoo.txt', 'w')
  texto = []
  texto.append("Parte da saida maquina turing -> Entrada da maquina post \n\n")
  texto.append("Tabela Traducao Estados: \n")
  for indx, name in enumerate(estados):
      texto.append(str(name)+"->"+estados[name]+"\n")
  texto.append("\nTabela Traducao Variavel:\n")
  for indx, name in enumerate(variavel):
      texto.append(str(name)+"->"+variavel[name]+"\n")
  arq.writelines(texto)
  arq.close()

leituraArquivo()
#imprimir()
turing()
letras()
#imprimir()
#imprTuring()
criarArquivosTuring()