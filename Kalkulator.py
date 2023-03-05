while True:
    try: # Szukanie wyjątku
        Symbols=input()
        Symbols=Symbols.split(' ')
        if Symbols[0]=='+':
            print(int(Symbols[1])+int(Symbols[2]))
        elif Symbols[0]=='-':
            print(int(Symbols[1])-int(Symbols[2]))
        elif Symbols[0]=='*':
            print(int(Symbols[1])*int(Symbols[2]))
        elif Symbols[0]=='/':
            print(int(Symbols[1])//int(Symbols[2])) # // ponieważ program oblicza ile liczb się mieści w drugiej np. 8//3 = 2
        elif Symbols[0]=='%':
            print(int(Symbols[1])%int(Symbols[2]))
    except EOFError: # Gdy SPOJ przestanie podawać liczby nastąpi EOFError, który powoduje wyłączenie programu 
        exit()