t=int(input()) #ilość testów
for _ in range(t):
    string=input()
    half=int(len(string)/2) #wyznaczenie połowy wyrazu
    print(string[:half]) #wypisanie połowy wyrazu