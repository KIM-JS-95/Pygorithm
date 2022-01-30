# TODO: 떡볶이 떡 만들기

def binery_search(array, target, start, end):
    mid = (start + end) // 2
    total = 0
    for x in array:
        if x > mid:
            total += x - mid

    if total < target:
        return binery_search(array, target, start, mid - 1)
    elif total > target:
        return binery_search(array, target, mid + 1, end)
    else:
        return mid

n, target = map(int, input().split(' '))

array = list(map(int, input().split()))

start = 0
end = max(array)
result = binery_search(array, target, start, end)

print(result)
