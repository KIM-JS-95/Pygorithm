# TODO: 안테나 (정렬)

n = int(input())
data = list(map(int, input().split()))
data.sort()

print(data[(n - 1) // 2])
