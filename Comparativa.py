import fileinput
import sys
from math import log
import time
import hashlib

def entropia(palabra):
    aux=0
    for a in palabra:
        N=int(ord(a))
        if N>aux:
            aux=N
    entr=len(palabra)*log(N,2)
    print("La entropia es: " + str(entr) + "\n")

if __name__ == '__main__':
    data=[]
    if sys.argv[1]== "-h":
        data=[]
        data.append(sys.argv[2])
        for palabra in data:
            InicioM=time.time()
            h=hashlib.new("md5")
            h.update(palabra.encode('utf-8'))
            print("El Hash es: " + h.hexdigest() + "\n")
            FinM=time.time()
            print("tiempo: " + str(FinM-InicioM)+ "\n")
            InicioS=time.time()
            h=hashlib.new("sha1")
            h.update(palabra.encode('utf-8'))
            print("El Hash SHA1 es: " + h.hexdigest() + "\n")
            FinS=time.time()
            print("tiempo: " + str(FinS-InicioS)+ "\n")
            InicioSHA=time.time()
            h=hashlib.new("sha256")
            h.update(palabra.encode('utf-8'))
            print("El Hash SHA256 es: " + h.hexdigest() + "\n")
            FinSHA=time.time()
            print("tiempo: " + str(FinSHA-InicioSHA)+ "\n")
    elif sys.argv[1]== "-a":
        data=[]
        TotalM=0
        TotalS=0
        TotalSHA=0
        file = open(sys.argv[2],encoding="Latin-1")
        for lines in file:
            data.append(lines.rstrip())
        for palabra in data:
            print(palabra)
            InicioM=time.time()
            h=hashlib.new("md5")
            h.update(palabra.encode('utf-8'))
            print("El Hash md5 es: " + h.hexdigest() + "\n")
            FinM=time.time()
            TotalM=TotalM+FinM-InicioM
            InicioS=time.time()
            h=hashlib.new("sha1")
            h.update(palabra.encode('utf-8'))
            print("El Hash SHA1 es: " + h.hexdigest() + "\n")
            FinS=time.time()
            TotalS=TotalS+FinS-InicioS
            InicioSHA=time.time()
            h=hashlib.new("sha256")
            h.update(palabra.encode('utf-8'))
            print("El Hash SHA256 es: " + h.hexdigest() + "\n")
            FinSHA=time.time()
            TotalSHA=TotalSHA+FinSHA-InicioSHA
        print("El tiempo md5 es: " + str(TotalM) + "\n")
        print("El tiempo SHA1 es: " + str(TotalS) + "\n")
        print("El tiempo SHA256 es: " + str(TotalSHA) + "\n")
    elif sys.argv[1]== "-e" and sys.argv[2]== "-h":
        data=[]
        data.append(sys.argv[2])
        for palabra in data:
            InicioM=time.time()
            h=hashlib.new("md5")
            h.update(palabra.encode('utf-8'))
            print("El Hash MD5 es: " + h.hexdigest() + "\n")
            FinM=time.time()
            entropia(h.hexdigest())
            print("tiempo: " + str(FinM-InicioM)+ "\n")
            InicioS=time.time()
            h=hashlib.new("sha1")
            h.update(palabra.encode('utf-8'))
            print("El Hash SHA1 es: " + h.hexdigest() + "\n")
            FinS=time.time()
            entropia(h.hexdigest())
            print("tiempo: " + str(FinS-InicioS)+ "\n")
            InicioSHA=time.time()
            h=hashlib.new("sha256")
            h.update(palabra.encode('utf-8'))
            print("El Hash SHA256 es: " + h.hexdigest() + "\n")
            FinSHA=time.time()
            entropia(h.hexdigest())
            print("tiempo: " + str(FinSHA-InicioSHA)+ "\n")

    elif sys.argv[1]== "-e" and sys.argv[2]== "-a":
        data=[]
        TotalM=0
        TotalS=0
        TotalSHA=0
        file = open(sys.argv[3],encoding="Latin-1")
        for lines in file:
            data.append(lines.rstrip())
        for palabra in data:
            print(palabra)
            InicioM=time.time()
            h=hashlib.new("md5")
            h.update(palabra.encode('utf-8'))
            print("El Hash md5 es: " + h.hexdigest() + "\n")
            FinM=time.time()
            entropia(h.hexdigest())
            TotalM=TotalM+FinM-InicioM
            InicioS=time.time()
            h=hashlib.new("sha1")
            h.update(palabra.encode('utf-8'))
            print("El Hash SHA1 es: " + h.hexdigest() + "\n")
            FinS=time.time()
            entropia(h.hexdigest())
            TotalS=TotalS+FinS-InicioS
            InicioSHA=time.time()
            h=hashlib.new("sha256")
            h.update(palabra.encode('utf-8'))
            print("El Hash SHA256 es: " + h.hexdigest() + "\n")
            FinSHA=time.time()
            entropia(h.hexdigest())
            TotalSHA=TotalSHA+FinSHA-InicioSHA
        print("El tiempo md5 es: " + str(TotalM) + "\n")
        print("El tiempo SHA1 es: " + str(TotalS) + "\n")
        print("El tiempo SHA256 es: " + str(TotalSHA) + "\n")