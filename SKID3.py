# Bartlomiej Pawelec WCY21KY2S1
from __future__ import print_function
import hashlib
import hmac 
import binascii

#Załozenia
#Deklaracja klucza tajnego K
key="0123456789ABCDEF"
keyh = binascii.unhexlify(key)

#Realizacja Protokolu
#Wejscie 
    #idA - Identyfikator uzytkownika A
    #idB - Identyfikator uzytkownika B
    #RandA - Losowa liczba uzytkownika idA
    #RandB - Losowa liczba uzytkownika idB
    #keyh - Tajny wspolny klucz A i B
#Wyjscie
    #HMACk(RandA,RandB,idB) - Klucz HMAC do potwierdzenia strony B
    #HMACk(RandB,idA) - Klucz HMAC do potwierdzenia strony A ( po potwierdzeniu B )
    
#Krok1 Deklaracja RandA i idA
def Krok1(Identyfikator_A,Liczba_losowa_A):
    idA=Identyfikator_A
    RandA=Liczba_losowa_A
    return idA,RandA

#Krok2 Deklaracja RandB, idB i obliczenie HMACk(RandA,RandB,B) przez B
def Krok2(Identyfikator_B,Liczba_losowa_B):
    idB=Identyfikator_B
    RandB=Liczba_losowa_B
    hmacb=hmac.new(keyh,RandA.str().encode()+RandB.str().encode()+idB.encode(),hashlib.sha3_512)
    hmacb_out = hmacb.hexdigest()
    return idB,RandB,hmacb_out

#Krok3 Obliczenie HMACk(RandA,RandB,B) przez strone A 
#      ,sprawdzenie strony B 
#      oraz obliczenie HMACk(RandB,A) przez strone A
def Krok3(idA,idB,RandA,RandB,hmacb_out):
    print("Strona A oblicza HMACk(RandA,RandB,idB)")
    hmaca=hmac.new(keyh,RandA.str().encode()+RandB.str().encode()+idB.encode(),hashlib.sha3_512)
    hmaca_out = hmaca.hexdigest()
    #Porownanie obliczonego HMACk(RandA,RandB,B) z tym obliczonym przez strone B
    if(hmaca_out==hmacb_out):
        print("Obliczone wartosci HMACk(RandA,RandB,B) przez strony A i B pokrywaja sie")
        print("Uzytkownik B jest potwierdzony, obliczanie HMACk(RandB,A)")
        hmaca=hmac.new(keyh,RandB.str().encode()+idA.encode(),hashlib.sha3_512)
        hmaca_out = hmaca.hexdigest()
        return hmaca_out
    else:
        print("Obliczone wartosci HMACk(RandA,RandB,B) przez strony A i B nie pokrywaja sie")
        print("Uzytkownik B jest niepotwierdzony")
        return -1
    
#Krok4 Obliczenie HMACk(RandB,A) przez B
#      i sprawdzenie strony A
def Krok4(idA,RandB,hmaca_out):
    print("Strona B oblicza HMACk(RandB,A)")
    hmacb=hmac.new(keyh,RandB.str().encode()+idA.encode(),hashlib.sha3_512)
    hmacb_out = hmacb.hexdigest()
    if(hmaca_out==hmacb_out):
        print("Obliczone wartosci HMACk(RandB,A) przez strony A i B pokrywaja sie")
        print("Uzytkownik A jest potwierdzony")
        return
    else:
        print("Obliczone wartosci HMACk(RandB,A) przez strony A i B nie pokrywaja sie")
        print("Uzytkownik A jest niepotwierdzony")
        return
    
###################################################
# Wykonanie protokolu
idA,RandA=Krok1("A",128)          #DELKARACJA IDENTYFIKATORA STRONY A ORAZ WYBRANEJ LICZBY
print("Strona o id: ",idA," wybrala losowa liczbe RandA: ",RandA)
print("Wyslanie RandA do strony B")

idB,RandB,HMAC_b1=Krok2("B",256)     #DELKARACJA IDENTYFIKATORA STRONY B ORAZ WYBRANEJ LICZBY
print("Strona o id: ",idB," wybrala losowa liczbe RandB: ",RandB)
print("Wartosc HMACk(RandA,RandB,idB) obliczonego przez strone B to: ")
print(HMAC_b1)
print("Wysylanie RandB,HMACk(RandA,RandB,idB) do strony A")

HMAC_a2=Krok3(idA,idB,RandA,RandB,HMAC_b1)
print("Wartosc HMACk(RandB,idA) obliczonego przez strone A to: ")
print(HMAC_a2)
print("Wysylanie HMACk(RandB,idA) do strony B")

if(HMAC_a2==-1):
    print("Koniec dzialania protokolu")
else:
    Krok4(idA,RandB,HMAC_a2)