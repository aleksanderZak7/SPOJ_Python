nk=input()
nk=nk.split(' ')
n=int(nk[0]) # ilość liczb
k=int(nk[1]) # o ile miejsc w lewo
Numbers=input()
Numbers=Numbers.split(' ')
for i in range(n):
    if(i+k<n):
        print(Numbers[i+k],end=' ')
    elif i+k==n:
        print(Numbers[n-(i+k)],end=' ')
    else:
        print(Numbers[-(n-(i+k))],end=' ')