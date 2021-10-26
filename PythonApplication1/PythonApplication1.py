from random import *
inimesed=[]
palgad=[]

def sisesta_andmed(i,p):
    N=4
    for n in range (N):
        inimene=input("nimi:")
        i.append(inimene)
        palk=randint(100,10000)
        p.append(palk)
    return i,p

def andmed_ekranile(i,p):
    N=len(i)
    for n in range(N):
        print(i[n],"-",p[n])

def kustutamine(i,p):
    nimi=input("Sisesta nimi,keda vaja kustuda:")
    n=i.count(nimi)
    abi_list=[]
    if n>0:
        t=0
        for e in range(len(i)):
            if i[e]== nimi:
                t+=1
                abi_list.append(int(e))
                print(t,"-",i[e],"-",p[e])
        j=int(input("Järjekordne number:"))   
        i.pop(abi_list[j-1])
        p.pop(abi_list[j-1])
        andmed_ekranile(i,p)
    return i,p

def suurim_palk(i,p):
    suurim=max(p)
    n=p.count(suurim)
    k_list=[]
    g=0
    if n>0:
        g+=1
        for k in range(len(p)):
            if i[k]==suurim:
                g+=1
                k_list.append((k))
    print(g,"-", i[k],"-",p[k])
    return i,p




def remove_person(i,p):
    remove_nimi=input("Nimi-")
    print(i.index(remove_nimi))
    p.pop(i.index(remove_nimi))
    i.pop(i.index(remove_nimi))
    return i,p

def sorteerimine(i,p):
    N=len(p)
    for n in range(0,N-1):
        for m in range(1,N+1):
            if p[n]<p[m]:
                abi=p[n]
                p[n]=p[m]
                p[m]=abi
                abi=i[n]
                i[n]=i[m]
                i[m]=abi
    andmed_ekranile(i,p)

while 1:
    print("k-kustutamine\na-andmete sisestamine\ne-andmed ekaranile-\nmax-kellel on suurim palk" )
    valik=input()
    if valik.lower()=="a":
        inimesed,palgad=sisesta_andmed(inimesed,palgad)
    elif valik.lower()=="e":
        andmed_ekranile(inimesed,palgad)
    elif valik.lower()=="k":
       inimesed,palgad=kustutamine(inimesed,palgad)
    elif valik.lower()=="r":
        inimesed,palgad==suurim_palk(i,p)
    else:
        break