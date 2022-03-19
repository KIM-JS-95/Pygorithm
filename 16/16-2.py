# TODO: 정수 삼각형 (p. 566)
#    왼쪽 위  / 위

n = int(input())

dp = []

for _ in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i + 1):

        if j == 0:
            up_left = 0
        else:
            up_left = dp[i - 1][j - 1]

        if j == i:
            up = 0
        else:
            up = dp[i - 1][j]

        dp[i][j] = dp[i][j] + max(up, up_left)

print(map(dp[n - 1]))
