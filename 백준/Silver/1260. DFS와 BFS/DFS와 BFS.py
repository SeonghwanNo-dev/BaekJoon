from collections import deque

a, b, c = map(int, input().split())

g = {}
# 모든 노드에 대해서 빈 리스트를 만들어 줘야 한다.
for i in range(a):
    g[i+1] = []

# 그래프 생성
for _ in range(b):
    i, j = map(int, input().split())
    g[i].append(j)
    g[j].append(i)  # 간선은 양방향이므로

# 그래프 안 노드 정렬
for i in range(a):
    g[i+1] = sorted(g[i+1])

        

visited = set()
def dfs(g, visited, s):
    visited.add(s)
    print(s, end=" ")
    for i in g[s]:
        if i not in visited:
            dfs(g, visited, i)

def bfs(g,s):
    visited = set([s])
    queue = deque([s])
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for i in g[node]:
            if i not in visited:
                visited.add(i)
                queue.append(i)

dfs(g, visited, c)
print() # 줄바꿈을 위해 빈 print() 함수 호출
bfs(g, c)