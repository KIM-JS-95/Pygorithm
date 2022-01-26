# TODO: 반씩 좁혀가는 탐색


def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1;


input_Data = input().split()

# 원소의 개수
n = int(input_Data[0])

target = input_Data[1]

array = input().split()

print(sequential_search(n, target, array))
