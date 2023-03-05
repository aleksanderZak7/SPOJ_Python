t=int(input())
for i in range(t):
    Numbers=input()
    Numbers=Numbers.split(' ')
    n=int(Numbers[0])
    x=int(Numbers[1])
    y=int(Numbers[2])
    L=[j for j in range(n) if j%x==0 if j%y!=0] # Utworzenie listy L pod warunkiem, że liczba jest podzielna przez x i nie jest podzielna przez y
    for j in L:
        print(j,end=' ') #wypisanie zawartości listy L
    print('') # odpowiada za enter po wypisaniu całej zawartości listy L