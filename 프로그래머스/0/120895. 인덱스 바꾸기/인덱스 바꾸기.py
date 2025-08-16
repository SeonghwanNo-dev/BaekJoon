def solution(my_string, num1, num2):
    
    # String 객체는 "불변 객체"다.
    # 따라서 리스트로 변환한 뒤 조작한다.
    
    my_string = list(my_string)

    temp = my_string[num1]
    my_string[num1] = my_string[num2]
    my_string[num2] = temp
    
    answer = "".join(my_string)
    return answer