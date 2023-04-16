while True:
    try:
        list_of_numbers = []
        data = input()
        data = data.split(' ')
        for i in range(len(data)):
            if i == 0:
                j = int(data[i]) - 1
            else:
                if int(data[i]) in list_of_numbers:
                    continue
                list_of_numbers.append(int(data[i]))
        list_of_numbers.sort(reverse = True)
        try:
            print(list_of_numbers[j])
        except:
            print('-')           
    except:
        break