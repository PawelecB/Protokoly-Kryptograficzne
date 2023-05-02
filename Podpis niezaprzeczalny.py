# Bartlomiej Pawelec WCY21KY2S1
from __future__ import print_function

#Realizacja Protokolu
#Wejscie
    #p - charakterystyka ciala (liczba pierwsza)
    #g - element pierwotny ciala Fp
    #x - klucz prywatny
    #X - klucz publiczny
    #m - wiadomosc
#Wyjscie 
    #s1a - wartosc obliczona przez uzytkownika A
    #s2a - wartosc obliczona przez uzytkownika A
    #s1b - wartosc obliczona przez uzytkownika B
    #s2b - wartosc obliczona przez uzytkownika B
    
#Generacja pary kluczy
def Krok1_key(m):
    p=next_prime(randint(2,2^16))
    F=GF(p)
    g=F.primitive_element()
    print("Liczba pierwsza p:",p," Element pierwotny g:",g)
    x=randint(1,(p-1))
    while gcd(x,(p-1))!=1:
        x=randint(1,(p-1))
    X=(g^x)%p
    return p,g,x,X

#Algorytm generacji podpisu     
def Krok1_gen(m,x,p):
    return (m^x)%p

#Protokol weryfikacji podpisu
#Krok1 B oblicza wartosc c
def Krok1(m,g,a,b,p):
    return ((m^a)*(g^b))%p

#Krok2 A oblicza s1 i s2
def Krok2(c,g,q,x,p):
    s1=(c*(g^q))%p
    s2=((c*(g^q))^x)%p
    return s1,s2

#Krok3 B przesyla a i b do A
def Krok3(a,b):
    print("Uzytkownik B wysyla do uzytkownika A wartosci a: ",a," i b: ",b)
    return

#Krok4 B oblicza s1 i s2
def Krok4(q,z,c,g,b,a,p):
    s1=(c*(g^q))%p
    s2=((X^(b+q))*z^a)%p
    return s1,s2

###################################################
# Wykonanie protokolu
#Generowanie zalozem
m=128   #Deklaracja wiadomosci
print("Zadeklarowana wiadomosc m=",m)
p,g,x,X=Krok1_key(m)
print("Podpisujacy A posiada pare kluczy: prywatny x=",x,",publiczny X=",X)
z=Krok1_gen(m,x,p)
print("Podpisujacy A wyznacza podpis z=",z)
a=randint(2,p)
b=randint(2,p)
print("Uzytkownik B wybiera liczbe losowa a=",a,"i b=",b)
c=Krok1(m,g,a,b,p)
print("Uzytkownik B oblicza c=",c,"i wysyla do A")
q=randint(2,p)
print("Uzytkownik A wybiera liczbe losowa q=",q)
s1a,s2a=Krok2(c,g,q,x,p)
print("Uzytkownik A oblicza s1=",s1a,"i s2=",s2a,"i wysyla do B")
Krok3(a,b)
print("Uzytkownik A wysyła wartosc q:",q,"do B")
s1b,s2b=Krok4(q,z,c,g,b,a,p)
print("Uzytkownik B oblicza s1=",s1b,"i s2=",s2b)
if s1a==s1b and s2a==s2b:
    print("Podpis jest poprawny")
else:
    print("Podpis jest niepoprawny")