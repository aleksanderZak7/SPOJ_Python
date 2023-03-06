def sorting(Point):
        Point=Point.split(' ')
        x=int(Point[1])
        y=int(Point[2])
        return x**2+y**2 #Odległość punktu od początku układu współrzędnych (bez pierwiastka)

t=int(input()) #liczba testów
for i in range(t):
    n=int(input()) #liczba punktów 
    P=[] #lista punktów
    for j in range(n):
            Point=input()
            P.append(Point)
    P.sort(key=sorting)
    for p in P:
        print(p)
    input() #jeden pusty wiersz na wejściu