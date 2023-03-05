import math
Day=86400 #ilosc sekund w jednym dniu
n=int(input()) #ilosc testow
for i in range(n):
    Result=0
    Information=input()
    Information=Information.split(' ')
    Quantity=int(Information[0]) #Ilość obżartuchów
    CookieBox=int(Information[1]) #ilość ciastek w 1 pudełku
    for j in range(Quantity):
        CookieTime=int(input()) #czas jedzenia 1 ciastka przez obżartucha
        Result+=math.floor(Day/CookieTime) #zaokrąglam w dół
    print(math.ceil(Result/CookieBox)) #zaokrąglam w góre, żeby nie kupić np. 2 i pół pudełka ciastek