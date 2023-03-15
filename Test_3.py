output = True #Warunek wypisywania liczb
forty_two = False #Czy poprzednia liczba była różna od 42
lifes = 3 #ilość po której zakończy się działanie programu
while True:
    try:# Szukanie wyjątku
        Number = int(input())
        if output:
            print(Number)
        if Number != 42:
            forty_two = True
        if Number == 42:
            if forty_two:
                forty_two = False
                lifes -= 1
                if lifes == 0:
                    output = False
    except EOFError: # Gdy SPOJ przestanie podawać liczby nastąpi EOFError, który powoduje wyłączenie programu 
        exit() 