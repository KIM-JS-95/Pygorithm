
def sol1():
    print("solution 2")
    global first, second, n,m,k
    result = 0
    while True:
        for i in range(k):
            if m==0:
                break
            result += first
            m -=1

        if m == 0:
            break
            result +=second
            m -=1
    print(result)

def sol2():
    print("solution 2")
    global first, second, n,m,k
    result = 0
    count = int(m/(k+1)) * k
    count += m % (k+1)

    result +=(count) * first
    result +=(m-count) * second
    print(result)


# Integer 타입으로 수집하고 공백으로 구분한다.
n,m,k = map(int, input().split())

# 리스트 타입으로 수집한다.
data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

sol1()

sol2()
