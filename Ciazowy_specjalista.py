D = int(input()) #ilość testów
for _ in range(D):
    Data = input()
    Data = Data.split(' ')
    X = float(Data[0])
    Y = float(Data[1])
    Z = float(Data[2])
    print(round(abs((12 / (Z - 1) * ((X + Y) - (Z * Y))))))

""" Obliczenia:
    Kid + X = Mom
    Kid + Y = (Kid + X + Y) / Z
    Z * Kid + Z * Y = Kid + X + Y
    (Z - 1) * Kid = X + Y - Z * Y
    Kid = ((X + Y) - (Z * Y)) / Z - 1
    Żeby otrzymać długość ciąży należy wynik pomnożyć przez 12:
    Wynik = 12 * ((X + Y) - (Z * Y)) / Z - 1"""