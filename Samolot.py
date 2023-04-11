data = input()
data = data.split(' ')
n1 = int(data[0]) #ilość rzędów w klasie biznesowej
k1 = int(data[1]) #ilość miejsc w jednym rzędzie klasy biznesowej
n2 = int(data[2]) #ilość rzędów w klasie ekonomicznej
k2 = int(data[3]) #ilość miejsc w jednym rzędzie klasy ekonomicznej
print(n1 * k1 + n2 * k2)