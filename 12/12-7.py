# TODO: 치킨 배달
from itertools import combinations


def sum(candidate):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        result += temp

    return result


if __name__ == "__main__":

    n, m = map(int, input().split())
    chicken, house = [], []

    for r in range(n):
        data = list(map(int, input().split()))
        for c in range(n):
            if data[c] == 1:
                house.append((r, c))  # 일반 집
            elif data[c] == 2:
                chicken.append((r, c))  # 치킨집

    candidate = list(combinations(chicken, m))

    result = 1e9
    for candidate in candidate:
        result = min(result, sum(candidate))

    print(result)