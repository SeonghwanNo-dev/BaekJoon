from collections import Counter

while(1):
    b = input()
    if b == "end":
        break
    
    a = list(b)
    temp_0 = ''
    v_count=0
    c_count=0

    dirty = 0
    # 제 1조건
    if 'a' in a or 'e' in a or 'i' in a or 'o' in a or 'u' in a:
        
        for i in a:  
            # 제 2 조건
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                v_count+=1
                c_count=0
                if(v_count>=3):
                    print(f"<{b}> is not acceptable.")
                    dirty=1
                    break
            else:
                v_count=0
                c_count+=1
                if(c_count>=3):
                    print(f"<{b}> is not acceptable.")
                    dirty=1
                    break
            
            # 제 3 조건
            temp_1 = i
            if(temp_0 == temp_1):
                if(temp_1=='e' or temp_1=='o'):
                    continue
                else:
                    dirty=1
                    print(f"<{b}> is not acceptable.")
                    break
            else:
                temp_0 = temp_1
        
        if(dirty==0):
           print(f"<{b}> is acceptable.")
        
    else:
        print(f"<{b}> is not acceptable.")

'''
# 문자열 삽입: fstring 방식이 가장 직관적이고, 실무에서도 많이 쓰인다.

name = "Python"
print(f"Hello {name} World")
'''