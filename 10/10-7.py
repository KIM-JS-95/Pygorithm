# TODO: 팀 결성

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

    for i in range(0, n + 1):
        parent[i] = i

    for i in range(m):
        oper, a, b = map(int, input().split())
        # NOTE: 팀 합치기
        if oper == 0:
            union(parent, a, b)
        # NOTE: 같은 팀 여부 확인
        elif oper == 1:
            # NOTE: 사이클 발생
            if find(parent, a) == find(parent, b):
                print("YES")
            else:
                print("NO")
