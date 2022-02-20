# TODO: 서로소 집합 : 공통 원소가 없는 집합

# NOTE: 두 집합 결합
def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# NOTE: 결합 전에 공통 원소 찾기
def find_parent(parent, x):
    # NOTE: 부모 배열의 원소가 자기 자신이 아닌 것은 루트 원소가 아님을 의미
    #       재귀로 루트 원소를 찾을 때 까지 반복
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


# L: -----------------------------------------------------------------------

if __name__ == "__main__":

    # NOTE: v : 노드개수
    #       e : 간선개수

    v, e = map(int, input().split())

    parent = [0] * (v + 1)

    # NOTE: 부모 테이블 상에서 부모를 자기 자신으로 초기화
    for i in range(1, v + 1):
        parent[i] = i

    for _ in range(e):
        a, b = map(int, input().split())
        union(parent, a, b)

    print('각 원소가 속한 집합: ', end=' ')

    for i in range(1, v + 1):
        print(find_parent(parent, i), end=' ')

    print()

    print('부모 테이블: ', end=' ')
    for i in range(1, v + 1):
        print(parent[i], end=' ')
