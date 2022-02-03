# TODO: 미래도시

# NOTE: 플로이드로 풀꺼야 모든 거점에서 가장 적은 비용으로
#  모든 거점으로 이동할 수 있는 거리를 구하고
#  정류/도착 지점만 선택하면 되니까
n, m = map(int, input().split())
INF = int(1e9)

graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신은 거리가 0 이야
for a in range(n+1):
    for b in range(n+1):
        if a== b:
            graph[a][b] =0

# 모든 거리는 1로 동일
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 정거 포인드 와 도착지를 선택하세요
station, end = map(int, input().split())

for k in range(n+1):
    for a in range(n + 1):
        for b in range(n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

distance = graph[1][end]+graph[station][end]
if distance >= INF:
    print(-1)
else:
    print(distance)