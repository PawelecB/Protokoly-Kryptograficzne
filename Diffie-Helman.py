# Bartlomiej Pawelec WCY21KY2S1
from __future__ import print_function

#4.1 Generacja parametrow dziedziny
# Wejscie
    # b– długość charakterystyki ciałapwyrażona w bitach
# Wyjscie
    # p– charakterystyka ciała Fp
    # n– rząd podgrupy cyklicznej
    # g– generator podgrupy cyklicznej rzędu n
def gen_dz(b):
    p=random_prime(2^(b-1),2^b)
    n=(p-1)//2
    while not is_prime(n):
        p=next_prime(p)
        n=(p-1)//2
    F=GF(p)
    g=F.random_element()
    while g.multiplicative_order()!=n or g^n!=1:
        g=F.random_element()
    return p,n,g

#4.2 Generator kluczy
# Wejscie 
    # p– charakterystyka ciała Fp
    # n– rząd podgrupy cyklicznej
    # g– generator podgrupy cyklicznej rzędu n
# Wyjscie
    # kpriv- klucz prywatny 
    # kpub- klucz publiczny
    
def gen_key(p,n,g):
    kpriv=randint(2,n-1)
    kpub=(g^kpriv)%p
    return kpriv,kpub

#4.3 Realizacja protokolu
# Wejscie 
    # p– charakterystyka ciała Fp
    # n– rząd podgrupy cyklicznej
    # g– generator podgrupy cyklicznej rzędu n
# Wyjscie
    # Informacja na temat rownosci otrzymanych kluczy sesyjnych 
#Krok1 Generacja dla strony A
def Krok1(p,n,g):
    Xa,Ka=gen_key(p,n,g)
    return Xa,Ka

#Krok2 Generacja dla strony B
def Krok2(p,n,g):
    Xb,Kb=gen_key(p,n,g)
    return Xb,Kb

#Krok3 Generacja dla strony C
def Krok3(p,n,g):
    Xc,Kc=gen_key(p,n,g)
    return Xc,Kc

#Krok4 Obliczenie klucza sesyjnego strony A i B
def Krok4(p, Kb, Xa):
    return (Kb^Xa)%p

#Krok5 Obliczenie klucza sesyjnego strony B i C
def Krok5(p, Kc, Xb):
    return (Kc^Xb)%p

#Krok6 Obliczenie klucza sesyjnego strony C i A
def Krok6(p, Ka, Xc):
    return (Ka^Xc)%p

#Krok7 Obliczenie klucza sesyjnego strony AB i C
def Krok7(p, Kab, Xc):
    return (Kab^Xc)%p

#Krok8 Obliczenie klucza sesyjnego strony BC i A
def Krok8(p, Kbc, Xa):
    return (Kbc^Xa)%p

#Krok9 Obliczenie klucza sesyjnego strony CA i B
def Krok9(p, Kca, Xb):
    return (Kca^Xb)%p

#Krok10 Porownanie otrzymanych kluczy sesyjnych
def Krok10(KS1,KS2,KS3):
    if(KS1==KS2 and KS2==KS3 and KS1==KS3):
        print('Klucze pokrywaja sie')
        return
    else:
        print('Klucze nie pokrywaja sie')
        return
    
#Generacja parametrow dziedziny
print('Generacja parametrow dziedziny')
p,n,g=gen_dz(20)  # DELKARACJA DLUGOSCI CIALA P W BITACH
print('p=',p)
print('n=',n)
print('g=',g)

#Krok1 Generacja liczb strony A
print('Krok1 Generacja liczb strony A')
Xa,Ka=Krok1(p,n,g)
print('Klucz prywatny strony A=',Xa)
print('Klucz publiczny strony A=',Ka)

#Krok2 Generacja liczb strony B
print('Krok2 Generacja liczb strony B')
Xb,Kb=Krok2(p,n,g)
print('Klucz prywatny strony B=',Xb)
print('Klucz publiczny strony B=',Kb)

#Krok3 Generacja liczb strony C
print('Krok3 Generacja liczb strony C')
Xc,Kc=Krok3(p,n,g)
print('Klucz prywatny strony C=',Xc)
print('Klucz publiczny strony C=',Kc)

#Krok4 Obliczenie klucza sesyjnego strony A i B
print('Krok4 Obliczenie klucza sesyjnego strony A i B')
KSab=Krok4(p,Kb,Xa)
print('Klucz sesyjny strony A i B=',KSab)

#Krok5 Obliczenie klucza sesyjnego strony B i C
print('Krok5 Obliczenie klucza sesyjnego strony B i C')
KSbc=Krok5(p,Kc,Xb)
print('Klucz sesyjny strony B i C=',KSbc)

#Krok6 Obliczenie klucza sesyjnego strony C i A
print('Krok6 Obliczenie klucza sesyjnego strony C i A')
KSca=Krok6(p,Ka,Xc)
print('Klucz sesyjny strony C i A=',KSca)

#Krok7 Obliczenie klucza sesyjnego strony AB i C
print('Krok7 Obliczenie klucza sesyjnego strony AB i C')
KSabc1=Krok7(p,KSab,Xc)
print('Klucz sesyjny strony AB i C=',KSabc1)

#Krok8 Obliczenie klucza sesyjnego strony BC i A
print('Krok8 Obliczenie klucza sesyjnego strony BC i A')
KSabc2=Krok8(p,KSbc,Xa)
print('Klucz sesyjny strony BC i A=',KSabc2)

#Krok9 Obliczenie klucza sesyjnego strony CA i B
print('Krok9 Obliczenie klucza sesyjnego strony CA i B')
KSabc3=Krok9(p,KSca,Xb)
print('Klucz sesyjny strony CA i B=',KSabc3)

#Krok10 Porownanie otrzymanych kluczy sesyjnych
print('Krok10 Porownanie otrzymanych kluczy sesyjnych')
Krok10(KSabc1,KSabc2,KSabc3)