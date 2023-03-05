D=int(input())
for _ in range(D):
	numbers=input()
	numbers=numbers.split(' ')
	Base=int(numbers[0])
	Exponent=int(numbers[1])
	if Exponent%4==0:
		Exponent=4
	else:
		Exponent=Exponent%4
	Result=Base**Exponent
	if Result>10:
		Result=str(Result)
		Result=Result[-1]
	print(Result)