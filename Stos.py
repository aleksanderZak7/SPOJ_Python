L=['','','','','','','','','','']
i=-1 # index w liście
while True:
    try: # Szukanie wyjątku
        Symbol=input()
        if Symbol=='+':
            i+=1 #dodanie elementu do stosu zwieksza indeks
            if i==(-1):
                i=0
            if i<10:
                number=int(input())
                L[i]=number
                print(':)')
            else:
                number=input()
                print(':(')
        elif Symbol=='-':
            if i==10:
                i=9
            if L[i]=='':
                print(':(')
            elif i>=0:
                print(L[i])
                L[i]=''
                i-=1 # wywalenie elementu ze stosu zmniejsza indeks
            else:
                print(':(')
    except EOFError: # Gdy SPOJ przestanie podawać liczby nastąpi EOFError, który powoduje wyłączenie programu 
        exit() 