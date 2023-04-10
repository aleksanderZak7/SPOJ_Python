while True:
    try:
        big_letters = False #wartość boolean sprawdzająca czy daną literę trzeba powiększyć
        output = ''
        line = input()
        for symbol in line:
            if symbol == '<': 
                big_letters = True #znak '<' sprawia że następne litery zwiększamy
                output += symbol
                continue
            elif symbol == '>':
                big_letters = False #znak '>' sprawia że następne litery nie są już zwiększane
                output += symbol
                continue
            if big_letters:
                output += symbol.upper() #zwiększanie danego znaku
                continue
            output += symbol
        print(output)
    except:
        exit(0)