def solution(rsp):
    rsp = list(rsp)
    r = []
    
    for i in rsp:
        if i == '0':
            r.append('5')
        if i == '2':
            r.append('0')
        if i == '5':
            r.append('2')
    
    
    answer = "".join(r)
    return answer