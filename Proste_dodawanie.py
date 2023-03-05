t=int(input())
for i in range(t):
    n=int(input())
    numbers=input() #Podaje liczby rozdzielone spacją
    numbers=numbers.split(' ')
    Result=0
    for j in range(n):
        Result+=(int(numbers[j])) #zamienione liczby z stringa na inta dodaje do wyniku
    print(Result)