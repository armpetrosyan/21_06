def find_factorial(a):
    res = 1
    for i in range(1, a+1):
        res *= i
    return res


num = int(input())

if num == 0:
    print(1)
else:
    pass

x = find_factorial(num)

print(x)
