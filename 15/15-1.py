# TODO: 정렬된 배열에서의 특정  수의 개수 구하기

def right_bi(arr, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if (mid == 0 or target > arr[mid - 1]) and target == arr[mid]:
        return mid

    elif arr[mid] >= target:
        return right_bi(arr, target, start, mid-1)

    else:
        return right_bi(arr, target, mid+1, end)


def left_bi(arr, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if (mid == n-1 or target < arr[mid + 1]) and target == arr[mid]:
        return mid

    elif arr[mid] > target:
        return left_bi(arr, target, start, mid-1)

    else:
        return left_bi(arr, target, mid+1, end)


n, x = map(int, input().split())
arr = list(map(int, input().split()))

a = left_bi(arr, x, 0, n-1)

print(a)
b = right_bi(arr, x, 0, n-1)

print(b)

count = a - b + 1

print(count)