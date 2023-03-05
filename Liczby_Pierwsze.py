def LiczbaPierwsza(liczba):
    for x in range(2,liczba//2+1): #Podaną liczbę sprawdzam poprzez podzielenie jej przez każdą liczbę całkowitą do wartości, która jest połową naszej liczby(dodatkowo dodaje 1 gdyby wyszła liczba niecałkowita)
        if liczba%x==0:
            return 'NIE'
    return 'TAK'
n=int(input()) #ilość testów
for i in range(n):
    number=int(input())#liczba do sprawdzenia
    if number<2:
        print('NIE')
    else: print(LiczbaPierwsza(number))