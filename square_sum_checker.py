# Use this program to check your list-style Square-Sum Hamiltonian Paths!

# This program works in python 3 ONLY

arr = list(map(int, input()[1:-1].split(', ')))
numbers = set([i for i in range(1, len(arr) + 1)])

last = None
for n in arr:
    if last is not None:
        if (n+last) ** 0.5 % 1 != 0:
            print("FAIL, Values do not add up to square number")
            break
    try:
        numbers.remove(n)
    except KeyError:
        print(n)
        print("FAIL, Incorrect number of values")
        break
    last = n
else:
    print("Success!")
