from collections import Counter

n = int(input())


for i in range(n):
    a = input()
    c= Counter(a)
    
    if ' ' in c:
        del c[' ']
    
    m = c.most_common(2)
    if len(m) < 2:
        print(m[0][0])
    else: 
        if(m[0][1] == m[1][1]):
            print('?')
        else:
            print(m[0][0])
