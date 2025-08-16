def solution(quiz):
    # 공백 -> a.split() 사용하면 good
    
    result = []
    for i in quiz:
        equ = i.split()
        for j in range(len(equ)):
            if equ[j] == "+":
                equ[j+1] = int(equ[j-1]) + int(equ[j+1]) - 2*int("0")
            if equ[j] == "-":
                equ[j+1] = int(equ[j-1]) - int(equ[j+1]) - 2*int("0")
            if equ[j] == "=":
                if int(equ[j+1]) - int("0") == equ[j-1]:
                    result.append("O")
                else:
                    result.append("X")
    
    answer = result
    return answer