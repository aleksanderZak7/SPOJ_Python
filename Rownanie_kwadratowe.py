while True: 
    try:
        coefficients=input()
        coefficients=coefficients.split(' ')
        A=float(coefficients[0])
        B=float(coefficients[1])
        C=float(coefficients[2])
        delta=B**2-4*A*C #Wzór na delte -> (b^2-4*ac)/4, jedank dzielenie przez 4 w tym przypadku jest zbedne
        if delta>0:
            print(2)
        elif delta==0:
            print(1)
        else:
            print(0)
    except EOFError: # Gdy SPOJ przestanie podawać liczby nastąpi EOFError, który powoduje wyłączenie programu 
        exit()