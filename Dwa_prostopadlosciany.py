first = input() #Pierwszy prostopadłościan
first = first.split(' ')
first_one = []
for number in first:
    first_one.append(int(number))
first_one.sort() #Posortowanie długości krawędzi prostopadłościanu
second = input() #Drugi prostopadłościan
second = second.split(' ')
second_one = []
for number in second:
    second_one.append(int(number))
second_one.sort() #Posortowanie długości krawędzi prostopadłościanu
if first_one[0] <= second_one[0] and first_one[1] <= second_one[1] and first_one[2] <= second_one[2]: #Warunki, które sprawdzają czy jeden może zmieścić w drugim
    print('tak')
elif first_one[0] >= second_one[0] and first_one[1] >= second_one[1] and first_one[2] >= second_one[2]:
     print('tak')
else:
    print('nie')