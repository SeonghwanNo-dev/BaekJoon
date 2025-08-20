def solution(emergency):
    # 원본 emergency 리스트를 훼손하지 않고 복사본을 만들어 내림차순 정렬
    sorted_emergency = sorted(emergency, reverse=True)
    
    # 순위를 저장할 빈 리스트 초기화
    answer = []
    
    # 원본 emergency 리스트를 순회하며 각 원소의 순위를 찾아서 answer에 추가
    for e in emergency:
        rank = sorted_emergency.index(e) + 1
        answer.append(rank)
        
    return answer