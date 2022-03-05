# TODO: 소수를 구하기 (485.p)
import math

m, n = map(int, input().split())
data = [True for _ in range(1000)]
data[1] = 0

for i in range(2, int(math.sqrt(n) + 1)):
    if data[i] == True:
        j = 2
        while i * j <= n:
            data[i * j] = False
            j += 1

for i in range(m, n + 1):
    if data[i]:
        print(i)
