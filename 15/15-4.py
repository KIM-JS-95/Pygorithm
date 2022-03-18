# TODO: 가사 검색
from bisect import bisect

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]


def count_q(arr, left_value, right_value):
    left = bisect(arr, left_value)
    right = bisect(arr, right_value)

    return right - left


arr = [[] for _ in range(10001)]
reversed_arr = [[] for _ in range(10001)]


def solution(words, queries):
    ans = []

    for word in words:
        arr[len(word)].append(word)
        reversed_arr[len(word)].append(word[::-1])

    for i in range(10001):
        arr[i].sort()
        reversed_arr[i].sort()

    for q in queries:
        if q[0] != "?":
            res = count_q(arr[len(q)], q.replace("?", "a"), q.replace("?", "z"))
        else:
            res = count_q(reversed_arr[len(q)], q[::-1].replace("?", "a"), q[::-1].replace("?", "z"))

        ans.append(res)
    print(ans)
    return ans


solution(words, queries)
