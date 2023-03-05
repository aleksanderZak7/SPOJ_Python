t=int(input())
for i in range(t):
    List = []
    Result=''
    Numbers =input()
    List=Numbers.split(' ')
    List.remove(List[0])
    List.reverse()
    for j in range(len(List)):
        if j < len(List)-1:
            Result +=List[j] + " "
        else:
            Result +=List[j]
    print (Result)