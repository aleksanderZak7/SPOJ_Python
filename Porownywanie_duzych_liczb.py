while(True):
    try:
        data = input()
        data = data.split(' ')
        if data[1] == '==':
            if data[0] == data[2]: #Gdy liczby są równe wypisuje 1
                print(1)
            else:
                print(0)
        elif data[1] == '!=':
            if data[0] != data[2]: #Gdy liczby nie są sobie równe wypisuje 1
                print(1)
            else:
                print(0)  
        elif data[1] == '>=':
            if len(data[0]) > len(data[2]): #Jeżeli lewa liczba ma więcej cyfr od drugiej to znaczy, że jest większa wieć wypisuje 1
               print(1)
            elif len(data[0]) == len(data[2]): #Jeśli obie liczby mają taką samą liczbę cyfr, porównuje cyfry każdej liczby po kolei
                left_number = [int(number) for number in data[0]]
                right_number = [int(number) for number in data[2]]
                for i in range(len(data[0])): 
                    if left_number[i] > right_number[i]:
                        print(1)
                        break
                    elif left_number[i] < right_number[i]:
                        print(0)
                        break
            else:
                print(0)
        elif data[1] == '<=':
            if len(data[0]) < len(data[2]): #Jeżeli prawa liczba ma więcej cyfr od drugiej to znaczy, że jest większa wieć wypisuje 1
               print(1)
            elif len(data[0]) == len(data[2]): #Jeśli obie liczby mają taką samą liczbę cyfr, porównuje cyfry każdej liczby po kolei
                left_number = [int(number) for number in data[0]]
                right_number = [int(number) for number in data[2]]
                for i in range(len(data[0])): 
                    if left_number[i] < right_number[i]:
                        print(1)
                        break
                    elif left_number[i] > right_number[i]:
                        print(0)
                        break
            else:
                print(0)
    except:
        break