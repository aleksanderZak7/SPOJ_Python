alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def letter_max_index(word):
    index = 0
    for letter in word:
        if(alphabet.index(letter) > index):
            index = alphabet.index(letter)
    return index

def letter_min_index(word):
    index = len(alphabet) - 1
    for letter in word:
        if(alphabet.index(letter) < index):
            index = alphabet.index(letter)
    return index

number_of_words = int(input())
for _ in range(number_of_words):
    word = input()
    print(letter_max_index(word) - letter_min_index(word))