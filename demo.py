def multi_increment(n):
    for i in range(2, n, i=i*2):
        print("Start", i)
        for j in range(i):
            print(i, j)


def factorial (n):
    if n == 0 :
        return 1
    else:
        return factorial(n - 1) * n

print(factorial(10))
