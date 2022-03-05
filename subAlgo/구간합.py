# TODO: 구간합을 계산하세요.

# NOTE: 모든 요소를 더하고 배열에 저장하여 구간 끝나는 점 - (구간 시작점-1)을 계산한다.

n = 5
data = [10, 20, 30, 40, 50]
prefix = [0]
sum = 0

for i in data:
    sum += i
    prefix.append(sum)

left = 3
right = 4
print(prefix[right] - prefix[left - 1])
