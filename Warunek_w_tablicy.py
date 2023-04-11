n = int(input()) #ilosć liczb całkowitych
numbers = []
output = []
for _ in range(n):
    number = int(input())
    numbers.append(number)
conditions = input()
conditions = conditions.split(' ')
condition = conditions[0] #warunek < x, albo > x
main_number = int(conditions[1])
if condition == '>':
    output = [number for number in numbers if number > main_number]
elif condition == '<':
    output = [number for number in numbers if number < main_number]
for number in output: #Wyświetlanie liczb, które spełniły podany wcześniej warunek
    print(number)