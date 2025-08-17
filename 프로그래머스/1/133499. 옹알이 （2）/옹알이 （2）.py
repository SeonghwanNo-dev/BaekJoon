def solution(babbling):
    
    word = ["aya", "ye", "woo", "ma"]
    num = ['0', '1', '2', '3']
    count = 0
    
    
    for i in babbling:
        for j in range(len(word)):
            if word[j] in i:
                i = i.replace(word[j], str(j))
                
        for k in range(len(i)):
            dirty = 0
            
            # 숫자인지 판별
            if i[k] not in num:
                dirty = 1
                break
            
            # 두 발음이 연속으로 나왔는지 판별
            if k == 0:
                continue
            else:
                if i[k] == i[k-1]:
                    dirty = 1
                    break
        if dirty ==0:
            count+=1
        
                
    
    answer = count
    return answer