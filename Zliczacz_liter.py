alfabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
n=int(input()) #ilosc testow
L=[]
S=set(L)
for i in range(n):
    x=input()
    x.replace(' ','')
    L.append(x) #zdania
    S.update(x) #zbiór liter w słowach
for i in alfabet:
    if i in S:
        Result=0
        for j in range(n):
            Result+=L[j].count(i)    
        print(i,Result)