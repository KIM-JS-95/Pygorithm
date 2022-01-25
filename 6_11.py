# TODO: 성적이 낮은 순으로 출력하기

n = int(input())

array = []
for i in range(n):
    intput_Data = input().split()
    array.append((intput_Data[0], int(intput_Data[1])))

array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=" ")
