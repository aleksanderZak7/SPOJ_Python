t = int(input()) #ilosć testów
for _ in range(t):
    Pesel = input() #Wzór na pesel podany w zadaniu:
    Result = int(Pesel[0]) * 1 + int(Pesel[1]) * 3 + int(Pesel[2]) * 7 + int(Pesel[3]) * 9 + int(Pesel[4]) * 1 + int(Pesel[5]) * 3 + int(Pesel[6]) * 7 + int(Pesel[7]) * 9 + int(Pesel[8]) * 1 + int(Pesel[9]) * 3 + int(Pesel[10]) * 1
    if str(Result)[len(str(Result)) - 1] == '0': #Sprawdzenie ostatniej literu wyniku
        print('D')
    else:
        print('N')