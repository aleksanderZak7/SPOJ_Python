def BMI_status(people): #Funkcja odpowiadająca za wypisanie odpowiednich osób
    for name in people:
        print(name)
    print()

t = int(input()) #ilość osób
Underweight = []
Optimal = []
Overweight = []
for _ in range(t):
    Data = input()
    Data = Data.split(' ')
    Name = Data[0]
    Mass = int(Data[1])
    Height = int(Data[2])/100
    BMI = Mass/(Height**2) #Obliczanie BMI
    if BMI < 18.5:
        Underweight.append(Name)
    elif BMI >= 18.5 and BMI < 25:
        Optimal.append(Name)
    else:
        Overweight.append(Name)
print('niedowaga')
BMI_status(Underweight)
print('wartosc prawidlowa')
BMI_status(Optimal)
print('nadwaga')
BMI_status(Overweight)