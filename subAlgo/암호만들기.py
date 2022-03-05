# TODO: 암호 만들기 (487.p)
import itertools

n, m = map(int, input().split())
v = ('a', 'e', 'i', 'o', 'u')
data = input().split()
data.sort()

for pw in itertools.combinations(data, n):
    # NOTE: 모음의 개수
    count = 0
    for i in pw:
        if i in v:
            count += 1

    # NOTE: 최소 한개의 모음과 최소 두개의 자음으로 구성
    if 1 <= count <= n - 2:
        print(''.join(pw))
