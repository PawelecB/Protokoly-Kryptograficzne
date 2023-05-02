# Bartlomiej Pawelec WCY21KY2S1
from __future__ import print_function

#Realizacja Protokolu
#Wejscie
    #M - Wiadomosc do podzielenia
    #n - Osoby uprawnione do odtworzenia wiadomosci
    #k - podzbior z n osob uprawnionych do odtworzenia wiadomosci
#Wyjscie 
    #xi - numer uzytkownika systemu
    #li - odpowiadajaca wartosc cienia f(xi)
    #p - liczba pierwsza 
    #M2 - Odtworzona wiadomosc 

#Krok1 Wyznaczenie liczby p
def Krok1(M,n):
    p=next_prime(M+n)
    return p

#Krok2 Generacja wielomianu
def Krok2(M,n,p):
    F=GF(p)
    P.<x>=F[]
    k=randint(2,n-1)
    f=M%p
    for i in range (1,k):
        f=f+F.random_element()*x^i
    return F,f,k;

#Krok3 Wyznaczenie cieni
def Krok3(f,n):
    xi=[]
    li=[]
    for i in range(0,n):
        xi.append(i+1)
    for i in range(0,n):
        li.append(f(xi[i]))
    return xi,li

#Krok4 Wyslanie uzytkownikom wartosci xi,li,p
def Krok4(xi,li,p,n):
    for i in range(0,n):
        print("Do osoby ",i+1," wysylana jest wartosc xi: ",xi[i]," li: ",li[i]," p: ",p)
    return

#Krok5 Wyznaczenie M
def Krok5(xi,li,k,p,F):
    D = zero_matrix(F,k,k)
    for i in range (0,k):
        for j in range (0,k):
            D[j,i]=xi[j]^i
    S=vector(F,[li[i] for i in range(k)])
    M=D.inverse()*S
    return M[0]

###################################################
# Wykonanie protokolu
M=1234      # Deklaracja wiadomosci M
n=10    # Deklaracja osob uprawnionych do odtworzenia wiadomosci
print("Zadeklarowana wiadomosc M: ",M)
p=Krok1(M,n)
print("Liczba p: ",p)
F,f,k=Krok2(M,n,p)
print("Wygenerowany wielomian: ",f)
xi,li=Krok3(f,n)
print("Wartosci cieni: ",li)
Krok4(xi,li,p,n)
M2=Krok5(xi,li,k,p,F)
print("Wyznaczona wiadomosc M: ",M2)
if(M==M2):
    print("Wiadomosci pokrywaja sie")
else:
    print("Wiadomosci nie pokrywaja sie")

    
    