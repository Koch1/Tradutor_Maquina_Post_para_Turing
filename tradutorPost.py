estados={}
variavel={}
estadoInicial=0
estadoAceite=[]
estadoRegeita=[]
regras=[]
estadoAtual=0
palavra=0
regrasMaquinaTuring=[]
import math

def imprimir():
    global estados,estadoInicial,estadoAceite,estadoRegeita, regras
    print("\nEstados: " + str(estados))
    print("\nEstados Inicial: " + str(estadoInicial))
    print("\nEstados Aceite : " + str(estadoAceite))
    print("\nEstados Rejeição : " + str(estadoRegeita))
    print("\nEstados Regras : " + str(regras))
    
def imprTuring():
    global estados,estadoInicial,estadoAceite,estadoRegeita, regras
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

def letras():
    global estados,estadoInicial,estadoAceite,estadoRegeita, regras
    if(len(estados)>len(variavel)):
        valor=len(estados)
    else:
        valor=len(variavel)
    est={}
    for indx, name in enumerate(estados):
        est['q'+str(converterd_b(name,valor))]=estados[name]
    estados=est
    estadoInicial=['q'+str(converterd_b(0,valor))]
    estAceito=[]
    for indx, name in enumerate(estadoAceite):
        estAceito.append('q'+str(converterd_b(name,valor)))
    estadoAceite=estAceito
    estReg=[]    
    for indx, name in enumerate(estadoRegeita):
        estReg.append('q'+str(converterd_b(name,valor)))
    estadoRegeita=estReg
    novaReg=[]
    for indx, name in enumerate(regras):
        regr=[]
        regr.append('q'+str(converterd_b(name[0],valor)))
        regr.append('a'+str(converterd_b(name[1],valor)))
        regr.append('q'+str(converterd_b(name[2],valor)))
        if(len(name)>3):
            regr.append('a'+str(converterd_b(name[3],valor)))
        novaReg.append(regr)
    regras=novaReg
        
def leituraArquivo():
    global estados,estadoInicial,estadoAceite, regras, estadoAtual, palavra,variavel
    bloco = open('teste.txt', 'r')
    #estados=bloco.readline().rstrip("\n\r").split(" ")
    estados[len(estados)]=bloco.readline().rstrip("\n\r")
    for val in bloco.readline().rstrip("\n\r").split(" "):
        v=True
        for est in estados:
            if(val==estados[est]):
                 estadoAceite.append(est)
                 v=False
        if(v):
            estados[len(estados)]=val
            estadoAceite.append(len(estados)-1)
    for  val in bloco.readline().rstrip("\n\r").split(" "):
        v=True
        for est in estados:
            if(val==estados[est]):
                 estadoRegeita.append(est)
                 v=False
        if(v):
            estados[len(estados)]=val
            estadoRegeita.append(len(estados)-1)
    while True:
        linha=bloco.readline().rstrip("\n\r")
        if(linha.find(' ')!=-1):
            reg=linha.split(" ")
            if(len(reg)==4):
                v1=True
                v2=True
                for est in estados:
                    if(reg[0]==estados[est]):
                        reg[0]=est
                        v1=False
                    if(reg[2]==estados[est]):
                        reg[2]=est
                        v2=False
                if(v1):
                    estados[len(estados)]=reg[0]
                    reg[0]=len(estados)-1
                if(v2):
                    estados[len(estados)]=reg[2]
                    reg[2]=len(estados)-1
                v1=True
                v2=True
                for var in variavel:
                    if(reg[1]==variavel[var]):
                        reg[1]=var
                        v1=False
                    if(reg[3]==variavel[var]):
                        reg[3]=var
                        v2=False
                if(v1):
                    variavel[len(variavel)]=reg[1]
                    reg[1]=len(variavel)-1
                if(v2):
                    variavel[len(variavel)]=reg[3]
                    reg[3]=len(variavel)-1
            elif(len(reg)==3):
                v1=True
                v2=True
                for est in estados:
                    if(reg[0]==estados[est]):
                        reg[0]=est
                        v1=False
                    if(reg[2]==estados[est]):
                        reg[2]=est
                        v2=False
                if(v1):
                    estados[len(estados)]=reg[0]
                    reg[0]=len(estados)-1
                if(v2):
                    estados[len(estados)]=reg[2]
                    reg[2]=len(estados)-1
                v1=True
                for var in variavel:
                    if(reg[1]==variavel[var]):
                        reg[1]=var
                        v1=False
                if(v1):
                    variavel[len(variavel)]=reg[1]
                    reg[1]=len(variavel)-1
            else:
                print("errro  nas regras");
            regras.append(reg)        
        else:
            palavra=linha
            break
    
leituraArquivo()
imprimir()
letras()
imprimir()
imprTuring()
