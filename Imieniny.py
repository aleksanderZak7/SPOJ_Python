D = int(input()) #Ilość testów
for _ in range(D):
    Data = input()
    Data = Data.split(' ')
    L = int(Data[0]) #ilość dzieci w klasie (łącznie z Jasiem)
    C = int(Data[1]) #ilość cukierków
    if L == 1:
        print('TAK')
    elif C % (L - 1) == 0:
        print('NIE')
    else:
        print('TAK')