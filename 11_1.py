# TODO: 모험가 길드

# NOTE: 전형적 그리디 문제

n = int(input())
array = list(map(int,input().split()))
array.sort()

count =0
group=0
for i in range(n):
    count +=1
    if count >=i:
        group +=1
        count=0

print(group)