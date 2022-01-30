# TODO: 부품찾기 (계수정렬)


n = int(input())
array = [0] * 100001

for i in input().split():
    array[int(i)] = 1

m = int(input())
target = list(map(int, input().split()))

for i in target:
    if array[i] == 1:
        print("yes")
    else:
        print("no")
