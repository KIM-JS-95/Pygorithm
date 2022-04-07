arr = [1, 4, 2, 5, 3]

summ = 0
for i in range(len(arr)):
    for j in range(1, len(arr) + 1, 2):
        if (j + i <= len(arr)):
            summ+=sum(arr[i:i + j])
print(summ)
