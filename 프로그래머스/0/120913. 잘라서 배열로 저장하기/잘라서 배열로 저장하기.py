def solution(my_str, n):
    
    a = len(my_str)//n
    answer = []
    
    for i in range(a):
        answer.append(my_str[i*n:(i+1)*n])
    
    if len(my_str)%n == 0:
        return answer
    
    answer.append(my_str[a*n:])
    return answer