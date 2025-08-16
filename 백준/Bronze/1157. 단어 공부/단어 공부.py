from collections import Counter

a = input()
a = list(a)

for i in range(len(a)):
    a[i]=a[i].upper()

c = Counter(a)
m = c.most_common(2)
if len(m) == 1:
    print(m[0][0])
else:
    if(m[0][1]==m[1][1]):
        print('?')
    else:
        print(m[0][0])