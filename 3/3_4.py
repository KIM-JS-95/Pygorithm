n,m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = max
    for j in data:
        min_value = min(min_value,j)

    result = max(min_value,result)

print(result)