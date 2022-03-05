# TODO: 투 포인터 구현 / 음수가 포함된 배열에서 원하는 구간 합의 개수를 구하라

def twopointer():
    n = 5
    m = 5
    data = [1, 2, 3, 2, 5]
    count = 0
    interval = 0
    end = 0
    for start in range(n):
        while interval < m and end < n:
            interval += data[end]
            end += 1

        if interval == m:
            count += 1

        interval -= data[start]
    print(count)


twopointer()
