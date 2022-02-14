
# TODO: 럭키 스트레이트
data = input()
length = len(data)
ans=0
for i in range(length//2):
    ans += int(data[i])

for i in range(length//2, length):
    ans -= int(data[i])

if ans ==0:
    print("LUCKY")
else:
    print("READY")