# TODO: 전보

# NOTE: 한 거점에서 모든 거점으로 이동하는데 걸리는 총시간
#   즉 다익스트라 문제 -> 우선순위 큐
import heapq

n, m, start = map(int, input().split())

INF = int(1e9)

graph = [[] for _ in range(n+1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))  # 자바 보다 편하지 않니?


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        # 현재 위치의 거리가 짧으면 패스
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

count = 0
max_distance = 0

for d in distance:
    if d != INF:
        max_distance = max(max_distance,d)
        count +=1
print(count,max_distance)
