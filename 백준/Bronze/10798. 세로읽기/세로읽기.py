from collections import deque

a = input()
b = input()
c = input()
d = input()
e = input()
m = deque()

a_list = deque(a)
b_list = deque(b)
c_list = deque(c)
d_list = deque(d)
e_list = deque(e)

it = []
it.append(len(a_list))
it.append(len(b_list))
it.append(len(c_list))
it.append(len(d_list))
it.append(len(e_list))
it.sort(reverse=True)

for _ in range(it[0]):
    if(len(a_list)>0):
        m.append(a_list.popleft())
    if(len(b_list)>0):
        m.append(b_list.popleft())
    if(len(c_list)>0):
        m.append(c_list.popleft())
    if(len(d_list)>0):
        m.append(d_list.popleft())
    if(len(e_list)>0):
        m.append(e_list.popleft())

s = ''.join(m)
print(s)

'''
# 리스트를 문자열로 바꾸는 법 

lst = ['h', 'e', 'l', 'l', 'o']
s = ''.join(lst)
print(s)  # hello

'''