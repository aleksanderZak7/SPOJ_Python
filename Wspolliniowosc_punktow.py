t = int(input()) #ilość testów
for _ in range(t):
    Data = input()
    Data = Data.split('\t')
    x = []
    y = []
    for i in range(0,6,2): # od 0 do 6 co drugą liczbę
        x.append(int(Data[i]))
        y.append(int(Data[1 + i]))
    if x[0] == x[1] == x[2] or y[0] == y[1] == y[2]:
        print('TAK')
    elif (x[0] * y[1]) + (x[1] * y[2]) + (y[0] * x[2]) - (y[1] * x[2]) - (x[0] * y[2]) - (y[0] * x[1]) == 0: #Wzór na Współliniowość trzech punktów -> http://www.algorytm.org/geometria-obliczeniowa/wspolliniowosc-trzech-punktow.html
        print('TAK')
    else:
        print('NIE')