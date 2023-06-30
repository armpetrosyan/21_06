count = 0
for i in range(2, 100):
    for j in range(2, 100):
        if (i % j) == 0 and i == j:
            print(i)
            count += 1
        elif (i % j) == 0 and i != j:
            break

print(f"{count} prime numbers!")
