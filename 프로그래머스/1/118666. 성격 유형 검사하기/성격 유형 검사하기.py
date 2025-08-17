from collections import defaultdict

def solution(survey, choices):
    
    d = defaultdict(int) # defaultdict 만들 때, 인자값 까먹으면 안됨!
    for i in range(len(choices)):
        if choices[i] == 4:
            continue
        elif choices[i] < 4:
            d[survey[i][0]] += 4 - choices[i]
        else:
            d[survey[i][1]] += choices[i] - 4
            

    answer = []
    if d['R'] > d['T']:
        answer.append('R')
    elif d['R'] < d['T']:
        answer.append('T')
    else:
        answer.append('R')
        
    if d['C'] > d['F']:
        answer.append('C')
    elif d['C'] < d['F']:
        answer.append('F')
    else:
        answer.append('C')
        
    if d['J'] > d['M']:
        answer.append('J')
    elif d['J'] < d['M']:
        answer.append('M')
    else:
        answer.append('J')
        
    if d['A'] > d['N']:
        answer.append('A')
    elif d['A'] < d['N']:
        answer.append('N')
    else:
        answer.append('A')
    
    answer = "".join(answer)
    return answer