# TODO: 외벽 점검(부르트 포스)
from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    # NOTE: 24시간 형태로 변환
    #  [1, 5, 6, 10, 13, 17, 18, 22]
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist)
    # NOTE: 약점 부분 전체 돌리기
    for start in range(length):

        # NOTE: [1, 2, 3, 4]
        for i in list(permutations(dist, len(dist))):
            cnt = 1
            position = weak[start] + i[cnt + -1]

            for index in range(start, start + length):

                if position < weak[index]:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    position = weak[start] + i[cnt + -1]
            answer = min(answer, cnt)

    if answer > len(dist):
        return -1
    return answer
