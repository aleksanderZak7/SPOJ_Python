def Newton_algorithm(x, y): #Algorytm Newtona potrzebny do obliczenia poprawnej odpowiedzi
    if x == y or y == 0:
        return 1
    Result = 1
    for i in range(y):
        Result *= x - i
    return Result / Factorial(y)

def Factorial(N): #silna z k
	base = 1
	for j in range(1, N+1):
		base *= j
	return base

T = int(input()) #ilość testów
for _ in range(T):
    data = input()
    data = data.split(' ')
    n = int(data[0])
    k = int(data[1])
    print(int(Newton_algorithm(n,k)))