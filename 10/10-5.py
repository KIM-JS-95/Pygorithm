# TODO: 최소 비용으로 모든 노드를 연결하자
#   크루스칼 알고리즘

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


# L: -----------------------------------------------------------------------


if __name__ == '__main__':
    v, e = map(int, input().split())

    parent = [0] * (v + 1)

    edges = []
    result = 0

    for i in range(1, v + 1):
        parent[i] = i

    # NOTE: 리스트에 넣는다.
    for _ in range(e):
        a, b, cost = map(int, input().split())
        edges.append((cost, a, b))

    # NOTE: 오름차순 정렬
    edges.sort()

    for edge in edges:
        cost, a, b = edge
        # NOTE: 사이클 판별
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            result += cost
    print(result)
