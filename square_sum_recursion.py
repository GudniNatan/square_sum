import threading
import time
from timeit import default_timer as timer
import sys


print("Choose length:")
count = int(input())
sqnum = list()
start = timer()
confirmed = list()

active = [True]
li = [i for i in range(count, 0, -1)]

for i in range(count, 1, -1):
    if i ** 2 < count * 2:
        sqnum.append(i ** 2)

def squareSum(i):
    seq = i
    if len(seq) == count or not active[0]:
        confirmed.append(seq)
        return
    for s in sqnum:
        n = s - seq[-1]
        if 0 < n <= count and n not in seq:
            squareSum(seq + [n])

def check(confirmed):
    if len(confirmed):
        active[0] = False
        print(confirmed[0])
        print(str(timer() - start), "sec runtime")
        active[0] = False
        for t in threading.enumerate():
            if t is not threading.currentThread():
                t.join()
        sys.exit(0)

for number in li:
    thread = threading.Thread(target=squareSum, args=([number],)).start()
    check(confirmed)


while len(threading.enumerate()) > 1:
    check(confirmed)
    time.sleep(1)

print("No solution was found")
