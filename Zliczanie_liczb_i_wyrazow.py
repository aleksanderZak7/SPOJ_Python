while(True):
    numbers = 0
    words = 0
    try:
        sentence = input()
        sentence = sentence.split(' ')
        for word in sentence:
            try:
                tmp = int(word) #Próba zamiany słowa na Integer, jak się uda to znaczy że to słowo jest liczbą, a jak nie to wyrazem
                numbers += 1
            except:
                words += 1
        print(str(numbers) + ' ' + str(words))
    except:
        break