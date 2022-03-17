# TODO: 고정점 찾기


def bi(arr, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if arr[mid] == mid:
        return mid
    elif arr[mid] < mid:
        return bi(arr, mid + 1, end)
    else:
        return bi(arr, start, mid - 1)


n = int(input())
arr = list(map(int, input().split()))

answer = bi(arr, 0, n)

if answer == None:
    print(-1)
else:
    print(answer)
