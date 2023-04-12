alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while True:
    try:
        sentence = input()
        output = ''
        for letter in sentence:
            if letter != ' ':
                index = alphabet.index(letter)
                output += alphabet[((index + 3) % len(alphabet))]
            else:
                output += letter
        print(output)
    except:
        break