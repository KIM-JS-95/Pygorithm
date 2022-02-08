# TODO: 1로 만들기


# NOTE: 탑-다운 (재귀)
def fun1(x):
    if x == 1:
        return 0
    if d[x] > 0:
        return d[x]
    d[x] = fun1(x - 1) + 1

    if x % 2 == 0:
        temp = fun1(x // 2) + 1
        if d[x] > temp:
            d[x] = temp

    if x % 3 == 0:
        temp = fun1(x // 3) + 1
        if d[x] > temp:
            d[x] = temp

    if x % 5 == 0:
        temp = fun1(x // 5) + 1
        if d[x] > temp:
            d[x] = temp
    return d[x]

# NOTE: 바텀-업 (반복)
def fun2(x):
    for i in range(2, x + 1):
        d[i] = d[i - 1] + 1

        if i % 2 == 0:
            d[i] = min(d[i], d[i//2] + 1)
        if i % 3 == 0:
            d[i] = min(d[i], d[i//3] + 1)
        if i % 5 == 0:
            d[i] = min(d[i], d[i//5] + 1)
    return d[x]

n = int(input())
d = [0] * (n + 1)
print(fun1(n))

print(fun2(n))
