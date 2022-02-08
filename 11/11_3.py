# TODO: 문자열 뒤집기


data = input()

tozero=0
toone=0

if data[0] == "1":
    tozero +=1
else:
    toone +=1

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            tozero += 1
        else:
            toone += 1


print(min(tozero,toone))