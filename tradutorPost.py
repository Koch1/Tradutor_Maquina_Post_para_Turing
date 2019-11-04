estados={}
variavel={}
estadoInicial=0
estadoAceite=[]
estadoRegeita=[]
regras={}
estadoAtual=0
palavra=0

def converterd_b(n,elemento):
    binario = ""
    while(True):
        binario = binario + str(n%2)
        n = n//2
        if n == 0:
            break
    binario = binario[::-1]
    print(len(binario));
    while True:
        if(len(binario)>elemento):
            break
        else:
            binario=str('0')+binario
    #binario = int(binario)
    #print(binario)
    return binario

def arquivo():
    global estados,estadoInicial,estadoAceite, regras,
    #for 

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
            estadoAceite.append(len(estados)-1)
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
            regras[len(regras)]=reg        
        else:
            palavra=linha
            break
    
leituraArquivo()
