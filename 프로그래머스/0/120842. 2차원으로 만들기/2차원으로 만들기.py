def solution(num_list, n):
    a = n
    b = len(num_list)//a
    
    answer = [[num_list[a*j+i] for i in range(a)] for j in range(b)]
    return answer