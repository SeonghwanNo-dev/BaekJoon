def solution(my_string):
    
    equ = my_string.split()
    n = len(equ)
    for i in range(n):
        if(equ[i] != "+" and equ[i] != "-"):
            
            # When Str -> Int, Have to deduct "0".
            # 3 = '3' - '0'
            equ[i] = int(equ[i]) - int("0")
    print(equ)

    
    for i in range(n):
        if (equ[i]=="+"):
            equ[i+1] = equ[i-1]+equ[i+1]
        if (equ[i]=="-"):
            equ[i+1] = equ[i-1]-equ[i+1]
        if (i == len(equ) - 1):
            answer = equ[i]

    return answer