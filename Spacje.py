import sys

SMS = ''
New_word = False
try:
    for line in sys.stdin: #Czytanie inputu dzieki bibliotece sys
        for letter in line: #rozdzielenie calej linii na slowa a potem na litery
            if letter != ' ':
                if New_word:
                    SMS += letter.upper()
                    New_word = False
                else:
                    SMS += letter
            elif letter == ' ': #napotkanie spacji powoduje zwiekszenie nastepnej litery
                New_word = True
    print(SMS)
except:
    exit(0)