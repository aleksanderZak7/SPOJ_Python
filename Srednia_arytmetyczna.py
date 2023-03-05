def medium(Lista): #funkcja obliczająca średnią z podanych liczb
    amount=0
    i=0
    for j in Lista:
        amount+=j
        i+=1
    mid=amount/i
    return mid
t=int(input())
for i in range(t):
    Numbers=input()
    Numbers=Numbers.split(' ')
    Numbers=Numbers[1:]
    L=[int(j) for j in Numbers]
    mid=medium(L)
    x=abs(L[0]-mid) #wartość |liczba-średnia|
    y=L[0]
    for j in L:
        if j==mid:
            y=j
            break
        elif abs(j-mid)<x:
            x=abs(j-mid)
            y=j
    print(y)