Data = input().split(' ') #Podanie współczynników a b i c
a = float(Data[0])
b = float(Data[1])
c = float(Data[2])
if b == c and a == 0: # 0/0 -> Nieskończenie Wiele Rozwiązań
    print('NWR')
elif a == 0: # (c - b != 0) / 0 -> Brak Rozwiązań
    print('BR')
else:
    Result = round((c - b) / a, 2)
    if int(Result) == Result:
        print(str(Result) + '0') #Bez tego wynik jest równy np. 0.0 co jest błędną odpowiedzią
    else:
        print(Result)
        
"""
a * x + b = c
a * x = c - b
x = (c - b) / a
"""