n=int(int(input()))
for _ in range(n):
    Numbers=input() #Podaje wszystkie liczby - jako string łącznie z liczbą, która opisuje ile poda znaków
    Numbers=Numbers.split(' ') #rozdzielam liczby spacją ponieważ są podawane co spacje
    Even=Numbers[1::2] #parzyste miejsca czyli o indeksie 0,2 itd
    Odd=Numbers[2::2] #nieparzyste czyli o indeksie 1,3 itd
    print(' '.join(Odd+Even)) #spoj patrzy na parzystość wliczając to liczbę która opisuje ile poda znaków więc zaczynam od indeksu 1 ;D