import math

def solution(num, total):
    
    middle = total / num

    
    a = math.ceil((middle - int(num/2)))
    b = int(middle + int(num/2))
    
    answer = []
    for i in range(a,b+1):
        answer.append(i)

    

    return answer