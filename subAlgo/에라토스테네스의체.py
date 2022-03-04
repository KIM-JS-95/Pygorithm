# TODO: 에라토스테네스의 체를 구현
import math


def Era():
    n = 1000
    arr = [True for _ in range(n + 1)]

    # NOTE: 탐색 범위를 반으로 줄이면 효율성 업!
    for i in range(2, int(math.sqrt(n)) + 1):
        j = 2
        while (i * j) <= n:
            arr[i * j] = False
            j += 1

    for i in range(2, n + 1):
        if arr[i]:
            print(i, end=' ')

Era()
