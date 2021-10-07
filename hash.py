import fileinput
def rellenar(palabra,pos):
    salt=["A","b","C","d","E"]
    if pos == len(salt):
        pos=0
    if len(palabra) <32:
        pal=palabra+salt[pos]
        pos=pos+1
        pal=rellenar(pal,pos)
        return pal
    else:
        return palabra

def hash(palabra,pos,Spos,aux):
    salt=["Z","W","R","Q","Y"]
    if Spos == len(salt):
        Spos=0
    if pos<len(palabra):
        A=int(ord(palabra[pos]))
        B=int(ord(salt[Spos]))
        C=len(palabra)
        if pos == 0:
            D=int(ord(palabra[pos+1]))
        elif pos%2 == 0:
            D=int(ord(aux[int(pos/2)]))
        else:
            D=int(ord(aux[pos-1]))
        aux.append(chr((B%A)+C+(D%A)))
        pos=pos+1
        Spos=Spos+1
        pal=hash(palabra,pos,Spos,aux)
        return pal
    else:
        return aux

def reducir(palabra,PosF,PosI,aux):
    if len(aux)==32:
        return aux
    else:
        A=ord(palabra[PosF])
        B=ord(palabra[PosI])
        posI=PosI+1
        posF=PosF-1
        aux.append(chr(A+B))
        pal=reducir(palabra,posF,posI,aux)
        return pal




def Iniciar(palabra):
    aux=[]
    aux2=''
    TamañoOriginal=len(palabra)
    if TamañoOriginal> 32:
        red=reducir(palabra,TamañoOriginal-1,0,aux)
        for v in red:
            aux2=aux2+v
        aux=[]
        f=hash(aux2,0,0,aux)
        aux2=''
        for v in f:
            aux2=aux2+v
        return aux2
    elif TamañoOriginal< 32:
        pal=rellenar(palabra,0)
        val=hash(pal,0,0,aux)
        for v in val:
            aux2=aux2+v
        return aux2
    else:
        return hash(palabra,0,0,aux)

if __name__ == '__main__':
    data=[]
    for lines in fileinput.input():
        data.append(lines.rstrip())
    for palabra in data:
        print("El Hash es: " + Iniciar(palabra) + "\n")