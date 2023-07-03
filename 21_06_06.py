def find_prime_factors(a):
    i = 2
    ls = []
    while i <= a:
        if a % i:
            i += 1
        else:
            a //= i
            ls.append(i)
    if a > 1:
        ls.append(a)
    return ls


num = int(input())

x = find_prime_factors(num)

print(x)
