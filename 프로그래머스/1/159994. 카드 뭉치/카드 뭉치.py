from collections import deque

def solution(cards1, cards2, goal):
    c1 = deque(cards1)
    c2 = deque(cards2)
    g = deque(goal)
    
    print(c1, c2, g)
    
    for _ in range(len(goal)):
        if len(c1)>0:
            a = c1.popleft()
        if len(c2)>0:
            b = c2.popleft()
        
        c = g.popleft()
        
        if a==c:
            c2.appendleft(b)
            a = ""
        elif b==c:
            c1.appendleft(a)
            b = ""
        else:
            return "No"

    return "Yes"