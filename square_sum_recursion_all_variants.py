# This variant of the program will show every single possible way to complete a Square-Sum Hamiltonian Path
# with the chosen number.
# Note that half of these are just the reverse of the other half.

import threading
import time
from timeit import default_timer as timer
import sys


print("Choose length:")
count = int(input())
sqnum = list()
start = timer()
confirmed = list()
printed = list()

active = [True]
new = [False]
li = [i for i in range(count, 0, -1)]

for i in range(count, 1, -1):
    if i ** 2 < count * 2:
        sqnum.append(i ** 2)

def squareSum(i):
    seq = i
    if len(seq) == count or not active[0]:
        confirmed.append(seq)
        new[0] = True
        return
    for s in sqnum:
        n = s - seq[-1]
        if 0 < n <= count and n not in seq:
            squareSum(seq + [n])

def check(confirmed):
    if len(confirmed):
        if new[0]:
            for seq in range(len(printed), len(confirmed)):
                print(confirmed[seq])
                printed.append(confirmed[seq])

for number in li:
    thread = threading.Thread(target=squareSum, args=([number],)).start()
    check(confirmed)


while len(threading.enumerate()) > 1:
    check(confirmed)
    time.sleep(1)

if len(confirmed) == 0:
    print("No solution was found")
print(str(timer() - start), "sec runtime")
