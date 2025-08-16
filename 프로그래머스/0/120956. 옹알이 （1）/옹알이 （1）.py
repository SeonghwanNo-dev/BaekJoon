def solution(babbling):
    r = 0
    for i in babbling:
        a = ["aya", "ye", "woo", "ma"]
        for j in a:
            if (j in i):
                # 문자열을 삭제할 땐, i = i.replace(j, "")를 사용한다.
                # 그러나 이렇게 바로 제거하면, 앞뒤 문자열이 붙어서 다른 패턴으로 인식될 수 있다.
                # 따라서 우선 임시 구분자(,)로 치환해 패턴 경계를 보존한 뒤, 나중에 제거할 것이다.
                i = i.replace(j, ",")
        # "," 제거
        i = i.replace(",", "")
        if(len(i)==0):
            r+=1
    
    answer = r
    return answer
