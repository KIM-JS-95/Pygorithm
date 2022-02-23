# TODO: 도시 분할 계획 (크루스칼 알고리즘)

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


if __name__ == '__main__':

    n, m = map(int, input().split())
    parent = [0] * (n + 1)

    for i in range(1, n + 1):
        parent[i] = i

    edges = []

    for _ in range(m):
        a, b, cost = map(int, input().split())
        edges.append((cost, a, b))

    # NOTE: 크루스칼 필수 오름차순 정렬하기
    # L: 리스트의 첫번째 배열을 기준으로 정렬하기 때문에
    #  코스트 오름차순으로 하기 위해서는 배열 앞으로 빼줘야함
    edges.sort()
    result = 0
    last = 0

    for edge in edges:
        cost, a, b = edge
        # NOTE: 사이클 발생하지 않는 조건으로
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            result += cost
            last = cost

    print(result - last)
