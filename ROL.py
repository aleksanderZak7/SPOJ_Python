n=int(input())
for _ in range(n):
    Numbers=input()
    Numbers=Numbers.split(' ')
    Numbers=Numbers[2:]+Numbers[1:2]
    print(' '.join(Numbers))