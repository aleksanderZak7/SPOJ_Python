D=int(input()) #Ilość zestawów danych
for _ in range(D):
    North_steps=0 #ilość kroków na północ
    West_steps=0 #ilość kroków na zachód
    well=0 #jak wartość well będzie równa 2 to skarb znajduje się w studni
    N=int(input()) #ilość wskazówek
    """ 0 - północ
        1 - południe
        2 - zachód
        3 - wschód """
    for i in range(N):
        moves=input()
        moves=moves.split(' ')
        direction=int(moves[0])
        steps=int(moves[1])
        if direction==0: #Kierunek północ
            North_steps+=steps
        elif direction==1: #Kierunek południe
            North_steps-=steps
        elif direction==2: #Kierunek zachód
            West_steps+=steps
        elif direction==3: #Kierunek wschód
            West_steps-=steps
    if North_steps==0:
        well+=1
    if West_steps==0:
        well+=1
    if well==2:
        print('studnia')
        continue
    if North_steps>0:
        print(f'0 {North_steps}')
    elif North_steps<0:
        print(f'1 {abs(North_steps)}') #wartość bezwględna ilości kroków na północ
    if West_steps>0:
        print(f'2 {West_steps}')
    elif West_steps<0:
        print(f'3 {abs(West_steps)}')   #wartość bezwględna ilości kroków na zachód