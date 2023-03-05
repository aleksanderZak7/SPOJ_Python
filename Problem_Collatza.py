"""Dany jest ciąg xn określony rekurencyjnie:
x0=s,
xn+1=3*xn+1, jeśli xn jest nieparzyste i
xn+1=xn/2, jeśli xn jest parzyste

Napisz program, który oblicza pierwsze takie n, dla którego xn=1."""
from math import floor
def Collatz(x):
    global n
    if x==1:
        print(n)
    elif x%2==0:
        n+=1
        Collatz(floor((x+1)/2)) #zaokrąglam w dół żeby program działał poprawnie (brak liczb niecałkowitych)
    else:
        n+=1
        Collatz(floor(3*x+1))  #zaokrąglam w dół żeby program działał poprawnie (brak liczb niecałkowitych)

t=int(input())
for i in range(t):
    Number=int(input())
    n=0
    Collatz(Number)