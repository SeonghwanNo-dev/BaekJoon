def solution(babbling):
    r = 0
    for i in babbling:
        a = ["aya", "ye", "woo", "ma"]
        for j in a:
            if (j in i):
                i = i.replace(j, ",")
        i = i.replace(",", "")
        if(len(i)==0):
            r+=1
    
    answer = r
    return answer