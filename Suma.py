Result=0
while True: 
    try: # Szukanie wyjątku
        Number=int(input())
        Result+=Number
        print(Result)
    except EOFError: # Gdy SPOJ przestanie podawać liczby nastąpi EOFError, który powoduje wyłączenie programu 
        exit()
    