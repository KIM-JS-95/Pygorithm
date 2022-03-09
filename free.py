dice = list(map(int, input().split()))
data = [0] * 7

for i in dice:
    data[i] += 1

answer = 0
if 3 == max(data):
    answer = 10000 + (data.index(3)) * 1000
if max(data) == 2:
    answer = 1000 + (data.index(2)) * 100
if max(data) == 1:
    answer = max(dice) * 100

print(answer)
