d=int(input()) #ilość testów
for _ in range(d):
    numbers=input()
    numbers=numbers.split(' ')
    a=int(numbers[0])
    b=int(numbers[1])
    r=a%b
    if r<0:
        r+=abs(b)
    print(r)