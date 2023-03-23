def change_system(n, system):
    Results = []
    Symbols = '0123456789ABCDEF'
    while n != 0 :
        Results.append(Symbols[int(n % system)]) #Reszta z dzielenia przez ilość znaków w systemie
        n = int(n/system)
    Result = ''
    for symbol in Results:
        Result = symbol + Result #Wypisanie odpowiedzi (dodajemy znak przed poprzedni wynik)
    return Result

t = int(input()) #ilość testów
for _ in range(t):
    n = int(input())
    hexadecimal_system = change_system(n,16) #zmiana na liczbe w systemie szesnastkowym
    eleventh_system = change_system(n,11) #zmiana na liczbe w systemie jedenastkowym
    print(hexadecimal_system + ' ' + eleventh_system)