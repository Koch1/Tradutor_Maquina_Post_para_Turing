estados={}
estTuring={}
variavel={}
varTuring={}
estadoInicial=0
estadoAceite=[]
estadoRejeita=[]
regras=[]
regrasTuring=[]
estadoAtual=0
palavra=0
import math

def imprimir():
    global estados,estadoInicial,estadoAceite,estadoRejeita, regras
    print("\nEstados: " + str(estados))
    print("\nVariavel: " + str(variavel))
    print("\nEstados Inicial: " + str(estadoInicial))
    print("\nEstados Aceite : " + str(estadoAceite))
    print("\nEstados Rejeição : " + str(estadoRejeita))
    print("\nEstados Regras : " + str(regras))
    
def imprTuring():
    global estados,estadoInicial,estadoAceite,estadoRejeita, regras
    print("EstadoAtual | Variave Ligo | Proximo Estado | Simobolo escrito |Movimento")
    for est in estados:
        for reg in regras:
            if(est==reg[0]):
                if(estados[est][0]=="R"):
                    if(estados[est][0]=="R"):
                        print("("+est+","+reg[1]+",")
                if(estados[est][0]=="A"):
                    print("("+est+","+"")
        
        

def converterd_b(n,elemento):
    binario = ""
    while(True):
        binario = binario + str(n%2)
        n = n//2
        if n == 0:
            break
    binario = binario[::-1]
    elem=int(math.log(elemento)/math.log(2))
    if(elemento%2):
        elem=elem+1
    while True:
        if(len(binario)>elem):
            break
        else:
            binario=str('0')+binario
    #binario = int(binario)
    #print(binario)
    return binario
#Traduz is estados para binario
def letras():
    global estados,estadoInicial,estadoAceite,estadoRejeita, regras
    if(len(estados)>len(variavel)):
        valor=len(estados)
    else:
        valor=len(variavel)
    est={}
    for indx, name in enumerate(estados):
        est['q'+str(converterd_b(name,valor))]=estados[name]
    estados=est
    var={}
    for indx, name in enumerate(variavel):
        var['a'+str(converterd_b(name,valor))]=variavel[name]
    variavel=val
    estadoInicial=['q'+str(converterd_b(0,valor))]
    estAceito=[]
    for indx, name in enumerate(estadoAceite):
        estAceito.append('q'+str(converterd_b(name,valor)))
    estadoAceite=estAceito
    estReg=[]    
    for indx, name in enumerate(estadoRejeita):
        estReg.append('q'+str(converterd_b(name,valor)))
    estadoRejeita=estReg
    novaReg=[]
    for indx, name in enumerate(regras):
        regr=[]
        regr.append('q'+str(converterd_b(name[0],valor)))
        regr.append('a'+str(converterd_b(name[2],valor)))
        regr.append('q'+str(converterd_b(name[3],valor)))
        novaReg.append(regr)
    regras=novaReg
        
def leituraArquivo():
    global estados,estadoInicial,estadoAceite, regras, estadoAtual, palavra,variavel
    bloco = open('novoCodigo.txt', 'r')
    #estados=bloco.readline().rstrip("\n\r").split(" ")
  #primeira linha
    estados[len(estados)]=bloco.readline().rstrip("\n\r")
  #segunda linha  q0001,q0111
    for val in bloco.readline().rstrip("\n\r").split(","):
        v=True
        for est in estados:
            if(val==estados[est]):
                 estadoAceite.append(est)
                 v=False
        if(v):
            estados[len(estados)]=val
            estadoAceite.append(len(estados)-1)
 #tercerira linha   q0001,q0111
    for  val in bloco.readline().rstrip("\n\r").split(","):
        v=True
        for est in estados:
            if(val==estados[est]):
                 estadoRejeita.append(est)
                 v=False
        if(v):
            estados[len(estados)]=val
            estadoRejeita.append(len(estados)-1)
#quartro ou mais
    while True:
        linha=bloco.readline().rstrip("( \n \r )").rstrip("(").replace("(","")
        if(linha.find(',')!=-1):
            reg=linha.split(",")
            if(len(reg)==4):
                v1=True
                v2=True
                for est in estados:
                    if(reg[0]==estados[est]):
                        reg[0]=est
                        v1=False
                    if(reg[3]==estados[est]):
                        reg[3]=est
                        v2=False
                if(v1):
                    estados[len(estados)]=reg[0]
                    reg[0]=len(estados)-1
                if(v2):
                    estados[len(estados)]=reg[3]
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
                print("errro  nas regras");
            regras.append(reg)        
        else:
            palavra=linha
            break
def turring ():
    global estados,estadoInicial,estadoAceite,estadoRejeita, regras,regrasTuring,varTuring,estTuring
    regr=[]
    branco=-1
    varTuring=[]
    for bra in variavel:
      if(variavel[bra]==''):
          branco=bra
      varTuring.append(bra)
    if(branco==-1):
      variavel[len(variavel)]=""
      branco=len(variavel)
    for regPost in regras:
        if(regPost[1]==''):
            regr.append([regPost[0],regPost[2],regPost[3],regPost[2],'d'])
        elif(regPost[1]=='d'):
            regr.append([regPost[0],regPost[2],regPost[3],branco,'d'])
        elif(regPost[1]=='i'):
            for var in varTuring:
                regr.append([regPost[0],var,regPost[0],branco,'d'])
            novoEst=(len(estados))-1
            estados[novoEst]="est"+str(novoEst)
            regr.append([regPost[0],branco,novoEst,regPost[2],'e'])
            for var in varTuring:
                regr.append([novoEst,var,regPost[3],branco,'e'])
    print(variavel)
    print(estados)
    for r in regr:
      print(r)
leituraArquivo()
imprimir()
turring ()
#letras()
#imprimir()
#imprTuring()
