# TODO: 사이클 판별 : 루트 노드가 서로 반복된다면?

# NOTE: 두 집합 결합
def union(parent, a, b):
    a = improved_find_parent(parent, a)
    b = improved_find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# L: -----------------------------------------------------------------------

# FIXME: 바효율적인 공통원소 조회를 어떻게 효율적으로 바꿀까?
#  부모 테이블의 값을 반환하도록 하여 공통 원소 값으로 갱신한다.

def improved_find_parent(parent, x):
    # NOTE: 부모 배열의 원소가 자기 자신이 아닌 것은 루트 원소가 아님을 의미
    #       재귀로 루트 원소를 찾을 때 까지 반복
    #       (비효율적이다. 시간 복잡도: O(N))
    if parent[x] != x:
        return improved_find_parent(parent, parent[x])
    return parent[x]


# L: -----------------------------------------------------------------------

if __name__ == "__main__":

    # NOTE: v : 노드개수
    #       e : 간선개수

    v, e = map(int, input().split())

    parent = [0] * (v + 1)

    # NOTE: 부모 테이블 상에서 부모를 자기 자신으로 초기화
    for i in range(1, v + 1):
        parent[i] = i

    cycle = False
    for _ in range(e):
        a, b = map(int, input().split())

# L: -----------------------------------------------------------------------
        #NOTE: 두 원소의 루트 노드가 반복된다면? (1-> 2 -> 3 -> 1 -> 2 -> 3 ....)
        if improved_find_parent(parent, a) == improved_find_parent(parent, b):
            cycle = True
            break
        else:
            union(parent, a, b)
# L: -----------------------------------------------------------------------

if cycle:
    print('Yes 사이클')
else:
    print('No 사이클')
