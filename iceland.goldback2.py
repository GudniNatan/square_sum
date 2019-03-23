import random

def MillerRabin(n, k=35):
    r = 0
    d = n - 1
    while d % 2 == 0:
        d /= 2
        r += 1

    for i in range(k):
        a = random.randint(2, n - 2)
        x = 1
        while d >= 1:
            if int(d) & 1:
                x = x * a % n

            d /= 2
            a = (a * a) % n

        if x == 1 or x == n - 1:
            continue
        for j in range(r-1):
            x = (x * x) % n
            if x == 1:
                return False
            if x == n - 1:
                break
        else:
            return False

    return True


def checkPrime(n):
    if n <= 1: return False
    elif n <= 3: return True
    elif n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

num = int(input())
a = 0

if num > 10000:
    for i in range(num - 4, 1, -2):
        if MillerRabin(i):
            num -= i
            a = i
            break
else:
    for i in range(num - 4, 1, -2):
        if checkPrime(i):
            num -= i
            a = i
            break

def eratosthenes(n):
    multiples = set()
    primes = list()
    for i in range(2, n + 1):
        if i not in multiples:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                multiples.add(j)
    return primes


primes = eratosthenes(num - 2)

for p in primes:
    if num - p in primes:
        print(str(a) + " "  + str(p) + " " + str(num - p))
        break