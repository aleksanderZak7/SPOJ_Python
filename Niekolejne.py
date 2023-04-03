from math import floor

n = int(input()) #Podana jedyna liczba
if n <= 2: 
    if n == 0:
        print(0)
    else:
        print('NIE')
else:
    print(n - int((n / 2)), end = ' ')
    for i in range(int(n / 2)):
        print(str(i) + ' ' + str((n - i)), end = ' ')
    if n % 2 != 0: #Jeśli liczba jest nieparzysta to floor zaokragla 0.5 na 1
        print((n - floor(n / 2)) - 1)