# TODO: 효율적인 화폐 구성

N, M = map(int, input().split())
currency = [int(input()) for _ in range(N)]

d = [10001] * (M+1)
d[0] = 0

for i in range(N):
    for j in range(currency[i], M+1):
        d[j] = min(d[j], d[j-currency[i]]+1)

if d[M] == 10001:
    print(-1)
else:
    print(d[M])