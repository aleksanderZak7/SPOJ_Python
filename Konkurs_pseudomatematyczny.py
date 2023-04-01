D = int(input()) #ilość testów
for _ in range(D):
    N = int(input()) #ilość punktów (nieistotna)
    Points = input()
    Points = Points.split(' ')
    Points = [int(Point) for Point in Points] #lista składana zamienia kazdy element listy string na int
    mx = max(Points) #wartość największa w liście
    how_many = 0 #ile razy występuję maksymalna ilość zdobytych punktów
    while mx in Points: #dopóki lista zawiera maksymalną liczbe zdobytych punktów to wartość jest usuwana a ilość jej występowania zwiększamy o 1
        Points.remove(mx)    
        how_many += 1
    Points.sort()
    output = '' #co wyświetle na koniec 
    for i in range(how_many):
        output += str(mx) + ' ' #max na poczatku, a potem posortowane inne liczby
    for Point in Points:
        output += str(Point) + ' '
    print(output)