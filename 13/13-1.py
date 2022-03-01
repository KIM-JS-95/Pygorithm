# TODO: 특정거리 도시 찾기 (큐: BFS는 시간초과)

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

# L-------------------------------------------------------------------------------

# TODO: 특정거리 도시 찾기 (백준 기준 다익스트라 : 우선순위 큐로 해결)


import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

distance = [INF] * (n + 1)
check= -1

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        # NOTE: 지나온 거리보다 비용이 더 클 경우
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i]= cost
                heapq.heappush(q, (cost, i))

dijkstra(x)

for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = 1
if check == -1:
    print(check)