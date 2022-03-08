# TODO: 연산자 끼워넣기(349.p)
#   주어진 배열과 operation을 사용하여 최대 값과 최솟값을 출력하자.

n = int(input())

# NOTE: 정해진 숫자 입력
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_num= -1e9
min_num = 1e9


def DFS(node, now):
    global add, sub, mul, div, max_num, min_num
    if node == n:
        max_num = max(max_num, now)
        min_num = min(min_num, now)
    else:
        if add > 0:
            add -= 1
            DFS(node + 1, now + numbers[node])
            add += 1
        if sub > 0:
            sub -= 1
            DFS(node + 1, now - numbers[node])
            sub += 1
        if mul > 0:
            mul -= 1
            DFS(node + 1, now * numbers[node])
            mul += 1
        if div > 0:
            div -= 1
            DFS(node + 1, now // numbers[node])
            div += 1


DFS(1, 0)
print(max_num)
print(min_num)
