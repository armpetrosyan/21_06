ls = [1, 11, 123, 1234]
ls2 = [1234, 123, 11]
ls3 = []


for i in ls:
    for j in ls2:
        if i == j:
            ls3.append(i)

print(ls3)
