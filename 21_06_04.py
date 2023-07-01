def print_pattern(a):
    ls = []
    res = a
    new = 0
    while a > 0:
        new = res - (a-1)
        ls.append(new)
        print(*ls)
        a = a-1


num = int(input('Input number : '))
if num == 0:
    print('Operation Invalid')
else:
    print_pattern(num)
