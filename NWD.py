import math
t=int(input()) #liczba testów
for _ in range(t):
    Numbers=input()
    Numbers=Numbers.split(' ')
    x=int(Numbers[0])
    y=int(Numbers[1])
    print(math.gcd(x,y))