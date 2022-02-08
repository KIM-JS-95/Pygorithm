# TODO: 만들 수 없는 금액 (그리디)


n = int(input())
array = list(map(int, input().split()))

# NOTE: 정석 방법
array.sort()

target = 1
for i in array:
    if target < i:
        break
    target += i

print(target)
