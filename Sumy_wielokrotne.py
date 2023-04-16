sum_of_tests = 0
while True:
    try:
        sum = 0
        data = input()
        data = data.split(' ')
        for number in data:
            sum += int(number)
        print(sum)
        sum_of_tests += sum
    except:
        break
print(sum_of_tests)