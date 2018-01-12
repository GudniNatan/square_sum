# Use this program to check your list-style Square-Sum Hamiltonian Paths!

# This program works in python 2 ONLY

arr = input()
numbers = set([i for i in range(1, len(arr) + 1)])

last = None
for n in arr:
    if last is not None:
        if (n+last) ** 0.5 % 1 != 0:
            print("FAIL, Values %d and %d do not add up to a square number" % (last, n))
            break
    try:
        numbers.remove(n)
    except KeyError:
        print("FAIL, Incorrect number of values. Either one appears twice or one is missing.")
        break
    last = n
else:
    print("Success!")
