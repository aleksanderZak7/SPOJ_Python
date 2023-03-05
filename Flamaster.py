C=int(input()) # ilość testów
for i in range(C):
    inscription=input()
    index=0
    for j in inscription: #Dla każdej litery w słowie
        if index==0:
            letter=j #pierwsza litera
            howmany=1 #ile razy występuję
            print(letter,sep='',end='')
            index+=1
        else:
            if j==letter: #jeśli się powtarza to ilość występowania zwiększamy o 1
                howmany+=1    
            else:
                if howmany>2: #jeśli podano nową litere i ilosć występowania jest większa niż 2 to wypisujemy ilość obok poprzedniej litery
                    print(howmany,sep='',end='')
                elif howmany >1:
                    print(letter,sep='',end='') #jeśli tylko raz się powtórzyła to dopisujemy ją drugi raz
                howmany=1
                letter=j
                print(letter,sep='',end='')
    if howmany>2: #sprawdzanie warunków dla ostatniej litery po wyjściu z pętli
        print(howmany,sep='',end='')
    elif howmany >1:
        print(letter,sep='',end='')
    print('')