# TODO: 커리큘럼 (위상정렬 알고리즘)
from collections import deque
import copy


def topology():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, v + 1):
        if inde[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            inde[i] -= 1

            if inde[i] == 0:
                q.append(i)

    for i in range(1, v + 1):
        print(result[i])


if __name__ == '__main__':
    # L: 노드 갯수
    v = int(input())
    inde = [0] * (v + 1)

    graph = [[] for i in range(v + 1)]
    time = [0] * (v + 1)

    for i in range(1, v + 1):
        data = list(map(int, input().split()))

        time[i] = data[0]

        for x in data[1:-1]:
            inde[i] += 1
            graph[x].append(i)

    topology()