def solution(my_string):
    for i in my_string:
        # isdigit은 str 객체의 메서드다. 기억하라.
        if(not str(i).isdigit()):
            my_string = my_string.replace(i, " ")
    
    my_string = my_string.split()
    sum = 0
    for j in my_string:
        sum+=int(j)-int("0")
        
    answer = sum
    return answer