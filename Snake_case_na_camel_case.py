Snake_case = input()
Camel_case = ''
underscore = False #Następna litera z dużej litery
for letter in Snake_case:
    if underscore:
        Camel_case += letter.upper()
        underscore = False
        continue
    if letter == '_':
        underscore = True
        continue
    Camel_case += letter
print(Camel_case)