for i in range(2, 100):
    for j in range(2, 100):
        if (i % j) == 0 and i == j:
            print(i)
        elif (i % j) == 0 and i != j:
            break
