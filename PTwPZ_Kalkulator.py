N = int(input()) #ilość zestawów danych
for _ in range(N):
    data = input()
    add = False
    substraction = False
    result = 0
    for symbol in data:
        if symbol == '+':
            add = True #Powoduje że następna liczba zostanie dodana do wyniku
        elif symbol == '-':
            substraction = True #Powoduje odejmowanie wyniku o następną liczbe
        else:
            if add:
                result += int(symbol)
                add = False
            elif substraction:
                result -= int(symbol)
                substraction = False
            else:
                result = int(symbol)
    print(result)