while(True):
    try:
        data = input()
        data = data.split(' ')
        a = float(data[0])
        b = float(data[1])
        c = float(data[2])
        output = 0 #Wynik programu
        if a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c >0: #Warunek istnienia trójkąta
            output = 1 #Spełnienie warunku powoduje zmiane wyświetlanego wyniku na 1
        print(output)
    except:
        break