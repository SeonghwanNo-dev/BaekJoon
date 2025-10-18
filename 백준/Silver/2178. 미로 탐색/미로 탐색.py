from collections import deque

n, m = map(int, input().split())
g = [list(map(int, input())) for i in range(n)]
# print(g)

visited = [[False]*m for _ in range(n)]
s = [0, 0]
def bfs(g, s, visited):
    # s는 [x, y]좌표로 이루어져 있음.
    # 여기다 level 정보도 추가
    s.append(1)
    queue = deque([s])
    visited[s[0]][s[1]] = True
    r = []
    global n
    global m
    
    while queue:
        i = queue.popleft()
        if 0<=i[0]-1<n and 0<=i[1]<m:
            if visited[i[0]-1][i[1]]==False and g[i[0]-1][i[1]]==1:
                queue.append([i[0]-1, i[1], i[2]+1])
                visited[i[0]-1][i[1]] = True
        if 0<=i[0]+1<n and 0<=i[1]<m:
            if visited[i[0]+1][i[1]]==False and g[i[0]+1][i[1]]==1:
                queue.append([i[0]+1, i[1], i[2]+1])
                visited[i[0]+1][i[1]] = True
        if 0<=i[0]<n and 0<=i[1]-1<m:
            if visited[i[0]][i[1]-1]==False and g[i[0]][i[1]-1]==1:
                queue.append([i[0], i[1]-1, i[2]+1])
                visited[i[0]][i[1]-1] = True
        if 0<=i[0]<n and 0<=i[1]+1<m:
            if visited[i[0]][i[1]+1]==False and g[i[0]][i[1]+1]==1:
                queue.append([i[0], i[1]+1, i[2]+1])
                visited[i[0]][i[1]+1] = True
                
        if i[0]==n-1 and i[1]==m-1:
            r.append(i[2])
        
    r = sorted(r, reverse=True)
    return r[0]

print(bfs(g, s, visited))