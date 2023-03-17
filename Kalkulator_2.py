Numbers = [0,0,0,0,0,0,0,0,0,0] #Pusta lista z 10 rejestrami
while True:
    try:
        Data = input()
        Data = Data.split(' ')
        Symbol = Data[0]
        a = int(Data[1])
        b = int(Data[2])
        if Symbol == 'z': #Nakazywanie zapisu podanej wartości na podany rejestr
            Numbers[a] = b
        elif(Symbol == '+'): 
            print(Numbers[a] + Numbers[b])
        elif(Symbol == '-'):
            print(Numbers[a] - Numbers[b])
        elif(Symbol == '*'):
            print(Numbers[a] * Numbers[b])
        elif(Symbol == '/'):
            print(int(Numbers[a] / Numbers[b]))
        elif(Symbol == '%'):
            print(Numbers[a] % Numbers[b])
    except:
        exit(0)