def solution(lottos, win_nums):
    
    # 우선 0의 개수를 구한다.
    a = lottos.count(0)
    # 일치하는 개수를 구한다
    b = 0
    for i in win_nums:
        if i in lottos:
            b+=1
    # 최악과 최선의 시나리오를 구한다.
    best = b+a
    worst = b
    # 그에 맞는 순위를 준다.
    best = 7 - best
    worst = 7 - worst
    
    if best == 7:
        best = 6
    if worst == 7:
        worst = 6
    
    answer = []
    answer.append(best)
    answer.append(worst)
    return answer