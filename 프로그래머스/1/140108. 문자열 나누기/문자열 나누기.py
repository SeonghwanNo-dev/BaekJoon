def solution(s):
    
    x_count = 0
    y_count = 0
    count = 0
    for i in range(len(s)):
        # 비어있다면 x 삽입
        if(x_count == 0):
            x = s[i]
            x_count+=1
        # 비어있지 않다면, x_count 증가 or y         
        else:
            if(s[i] == x):
                x_count+=1
            else:
                y_count+=1
        if x_count == y_count:
            count+=1
            x_count = 0
            y_count = 0
    
    if(x_count != 0):
        count+=1
        
    answer = count
    return answer