import random, timeit
n = int(input("test number: "))
k = int(input("accuracy level: "))


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

start = timeit.timeit()
print(MillerRabin(n, k))
end = timeit.timeit()
print(end - start)
