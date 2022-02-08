# TODO :1로 계산되는 최소 횟수를 반환하라
# 1로 만들기
# N에서 1을 뺀다  / N을 K로 나눈다

n, k = map(int, input().split())

answer = 0

while n >= k:
    while n % k != 0:
        n -= 1
        answer += 1
    n //= k
    answer +=1

while n > 1:
    n -= 1
    answer += 1

print(answer)
