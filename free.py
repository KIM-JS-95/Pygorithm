from itertools import combinations

n = int(input())
data = []
member = [i for i in range(1, n+1)]

for i in range(n):
    data.append(list(map(int, input().split())))


team = []
for x in list(combinations(member, n//2)):
    team.append(x)

min_value = 1e9

for i in range(n//2 -1):
    for j in range(i+1, n//2):
        link = data[team[i]][team[j]] + data[team[i]][team[j]]
        start = data[team[i]][team[j]] + data[team[i]][team[j]]
        min_value = min(abs(link - start), min_value)


print(min_value)