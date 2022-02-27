# TODO: 특정거리 도시 찾기 (큐)

# NOTE: 도시개수 / 도로개수 / 거리정보 / 출발 도시의 번호
from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)

dist = [-1] * (n + 1)
dist[x] = 0;

print([x])
q = deque([x])
while q:
    now = q.popleft()

    for node in graph[now]:
        if dist[node] == -1:
            dist[node] = dist[now] + 1
            q.append(node)
    flag = False
for i in range(n + 1):
    if dist[i] == k:
        print(i)
        flag = True

if not flag:
    print(-1)
