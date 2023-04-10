n = int(input()) #liczba miast na trasie
sum = 0 #suma zarobionych pieniedzy
profit = 0 #zysk z koncertów
for _ in range(n):
    money = int(input())
    sum += money
    if sum > profit: #Jeżeli suma pieniędzy z koncertów jest większa od całego zysku to zysk zmienia wartość na tą sumę
        profit = sum
    if sum < 0:
        sum = 0
print(profit)