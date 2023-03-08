while True: 
    try:
        numbers=input()
        numbers=list(numbers.split(' '))
        numbers.reverse() #ODwrócenie kolejności listy podanych liczb
        for number in numbers:
            print(number,end=' ')
        print()
    except EOFError: # Gdy SPOJ przestanie podawać liczby nastąpi EOFError, który powoduje wyłączenie programu 
        exit()