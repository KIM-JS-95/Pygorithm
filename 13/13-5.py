# TODO: 감시 피하기(351.p)
#   오브젝트 설치를 최소화 하여 선생님 들의 감시를 피하자


from itertools import combinations

n = int(input())
graph = []
teacher = []
space = []


def process():
    for x, y in teacher:
        # NOTE: 방향 (0 ~ 3)
        for i in range(4):
            if BFS(x, y, i):
                return True
    return False


def BFS(x, y, dir):
    if dir == 0:
        # NOTE: 오른쪽
        while n > x:
            check(x, y)
            x += 1
        # NOTE: 왼쪽
    if dir == 1:
        while x >= 0:
            check(x, y)
            x -= 1
    # NOTE: 위
    if dir == 2:
        while n > y:
            check(x, y)
            y += 1
    # NOTE: 아래
    if dir == 3:
        while y >= 0:
            check(x, y)
            y -= 1

    return False


def check(x, y):
    if graph[x][y] == 'S':
        return True
    if graph[x][y] == 'O':
        return False


# NOTE: 맵
for i in range(n):
    graph.append(list(input().split()))
    for j in range(n):
        if graph[i][j] == 'T':
            teacher.append((i, j))
        if graph[i][j] == 'X':
            space.append((i, j))

find = False

# NOTE: 빈 공간에서 무작위로 3개의 공간을 선택하여 오브젝트 설치
for data in combinations(space, 3):
    for x, y in data:
        graph[x][y] = 'O'

    # NOTE: 학생을 발견하지 못했다면
    if not process():
        # NOTE: 오브젝트를 설치할 조건의 위치를을 찾음
        find = True
        break

    # NOTE: 찾지 못했다면 다시 돌려놓음
    for x, y in data:
        graph[x][y] = 'X'

if find:
    print("found it!")
else:
    print("Not Found")
