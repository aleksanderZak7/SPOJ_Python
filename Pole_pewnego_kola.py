import math
Numbers=input()
Numbers=Numbers.split(' ')
r=float(Numbers[0]) #Stringa zamieniam na float, żeby uniknąć błędu gdy podane zostaną liczby zmiennoprzecinkowe
d=float(Numbers[1])
S=round(math.pi*(r**2-(d/2)**2),2) #Zaokrąglam do 2 miejsc po przecinku
print(S) #Podaje liczbę zmiennoprzecinkową S oznaczającą pole koła 