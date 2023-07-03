while True:
    res = 0
    num1 = float(input('Enter your first number: '))
    opr = input('Enter your operator(*, +, -, /): ')
    num2 = float(input('Enter your second number: '))
    if opr == '*':
        res = num1*num2
    if opr == '+':
        res = num1 + num2
    if opr == '-':
        res = num1 - num2
    if opr == '/':
        if num2 == 0:
            print('UNDEFINED')
        else:
            res = num1 / num2
    print(res)
    ext = input('E-exit / C- Continue: ')
    if ext == 'E':
        break
