"""
Wzór na prędkość średnią znając obie prędkości i wiedzać, że pokonujemy taką samą drogę w obie strony:

Vśr=S1+S2(cała droga)/t(czas w jakim pokonaliśmy droge w obu kierunkach)
t=t1+t2
t1=S1/V1
t2=S2/V2
t=S1/V1+S2/V2
S1=S2
t=(V2S+V1S)/V1*V2=S*(V1+V2)/V1V2

Vśr=2S/S*(V1+V2)/V1V2=2S*((V1*V2)/S*(V1*V2)) -> S skracamy
Vśr=(2*V1*V2)/(V1+V2)
"""
t=int(input())
for t in range(t):
    Speed=input()
    Speed=Speed.split(' ')
    V1=int(Speed[0]); V2=int(Speed[1]) #wczytanie V1 i V2
    print(round((2*V1*V2)/(V1+V2))) #wynik podajemy w przybliżeniu