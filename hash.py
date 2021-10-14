import fileinput
import sys
from math import log
def rellenar(palabra,pos):
    #cEsta funcion rellena una palabra menor a 32 caracteres con los caracteres contenidos en salt, se termina al tener 32 caracteres.
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
    #recibe una palabra de 32 caracteres, con la funcion ord se calcula el valor en unicode de un caracteres y chr lo decodifica a string.
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
        E=int((B%A)+C+(D%A))
        if (E<127):
            X=E
        else:
            if (E%2==0 and E<257):
                X=int(E/2+A)
            else:
                X=int(ord(salt[Spos])+A)
        aux.append(chr((X)))
        pos=pos+1
        Spos=Spos+1
        pal=hash(palabra,pos,Spos,aux)
        return pal
    else:
        return aux

def reducir(palabra,PosF,PosI,aux):
    #reduce una palabra mayor a 32 digitos, para esto suma el valor unicode en digitos de la palabra en las posiciones PosF y PosI, las cuales comienzan en el final e inicio respectivamete, luego lo agrega al auxiliar.
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
    #verifica el tamaño de la palabra, llama a la funcion adecuada y retorna la palabra hasheada.
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
        aux=[]
        aux2=''
        pal=rellenar(palabra,0)
        val=hash(pal,0,0,aux)
        for v in val:
            aux2=aux2+v
        return aux2
    else:
        aux=[]
        return hash(palabra,0,0,aux)

def entropia(palabra):
    aux=0
    if len(palabra)==32:
        for a in palabra:
            N=int(ord(a))
            if N>aux:
                aux=N
        entr=len(palabra)*log(N,2)
        print("La entropia es: " + str(entr))
    else:
        print("Error: la palabra no posee 32 caracteres")

if __name__ == '__main__':
    data=[]
    if sys.argv[1]== "-h":
        data=[]
        data.append(sys.argv[2])
        for palabra in data:
            print("El Hash es: " + Iniciar(palabra) + "\n")
    elif sys.argv[1]== "-a":
        data=[]
        data.append(sys.argv[2])
        for lines in fileinput.input(sys.argv[2]):
            data.append(lines.rstrip())
        for palabra in data:
            print("El Hash es: " + Iniciar(palabra) + "\n")
    elif sys.argv[1]== "-e" and sys.argv[2]== "-h":
        data=[]
        data.append(sys.argv[3])
        for palabra in data:
            h=Iniciar(palabra)
            print("El Hash es: " + h + "\n")
            entropia(h)

    elif sys.argv[1]== "-e" and sys.argv[2]== "-a":
        data=[]
        data.append(sys.argv[2])
        for lines in fileinput.input(sys.argv[2]):
            data.append(lines.rstrip())
        for palabra in data:
            h=Iniciar(palabra)
            print("El Hash es: " + h + "\n")
            entropia(h)