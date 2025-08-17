from collections import deque

def solution(A, B):
    a = deque(A)
    b = deque(B)
    
    dirty = 0
    count = 0
    
    for _ in range(len(a)):
        if(a == b):
            dirty = 1
            break
        temp = a.pop()
        a.appendleft(temp)
        count+=1
    
    if(dirty == 0):
        answer = -1
    else:
        answer = count
        
    return answer