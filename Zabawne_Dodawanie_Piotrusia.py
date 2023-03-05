def palindrom(x,trials):
    if x==x[::-1]: #sprawdzam czy dana liczba jest palindromem
        print(x,trials)
    else:
        x=str(int(x)+int(x[::-1])) #jesli nie to do podanej liczby dodaje wartość liczby od prawej i sprawdzam ponownie
        trials+=1
        palindrom(x,trials)
        
t=int(input()) #ilość testów
for i in range(t):
    number=input()
    if number==number[::-1]: #sprawdzam czy dana liczba jest palindromem
        print(number,0)
    else:
        how_many=0
        palindrom(number,how_many)
    