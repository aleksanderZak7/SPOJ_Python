import math

N=int(input()) #ilość testów
for _ in range(N):
    data=input()
    data=data.split(' ')
    a=int(data[0]) #Pierwsza grupa
    b=int(data[1]) #Druga grupa
    Result=lambda x,y:x*y//math.gcd(x,y)  #Do obliczenia NWW(Największą wspólną wielokrotność) wykorzystuję NWD(Najwięlszy wspólny dzielnik)
    print(Result(a,b))