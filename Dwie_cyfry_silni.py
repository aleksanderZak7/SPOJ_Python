D=int(input()) #ilość testów
for _ in range(D):
    number=int(input())
    if number>9:
        print('0 0') 
        continue
    else:
        Factorial=1
        for x in range(1,number+1):
            Factorial*=x 
    STRING=str(Factorial)
    STRING='0'+STRING
    print(' '.join(STRING[-2:]))