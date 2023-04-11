while(True):
    try:
        data = input()
        c = data[0:1] #litera, która należy usunąć z napisu
        sentence = data[2:]
        while(c in sentence): #Pętla wykonująca się tak długo dopóki c znajduję się w sentence
            sentence = sentence.replace(c,'')
        print(sentence)
    except:
        break