def Game(a,b):
    while b:
        x =a%b
        a=b
        b=x
    return a*2
        
t=int(input()) #ilość testów
for _ in range(t):
    tokens=input()
    tokens=tokens.split(' ')
    tokens_a=int(tokens[0])
    tokens_b=int(tokens[1])
    print(Game(tokens_a,tokens_b))