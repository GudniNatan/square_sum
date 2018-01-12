import threading
import time
from timeit import default_timer as timer
import sys

print("Choose length:")
count = int(input())

start = timer()

li = [i for i in range(count, 0, -1)]

sqnum = list()
for i in range(2, int((count ** 0.5) * 1.5) + 3):
    if i ** 2 < count * 2:
        sqnum.append(i ** 2)

sqnum.reverse()
confirmed = list()
active = [True]

def squareSum(startNum):
    cur = startNum
    seq = list()
    tested = set()
    while active[0]:
        seq.append(cur)
        if len(seq) == count:
            confirmed.append(seq)
            return seq
        for s in sqnum:
            candidate = s - cur
            if 0 < candidate <= count and candidate not in seq:
                if tuple(seq + [candidate]) in tested:
                    continue
                cur = candidate
                break
        else:
            tested.add(tuple(seq))
            seq.pop()
            if len(seq) == 0:
                return None
            cur = seq.pop()

def check(confirmed):
    if len(confirmed):
        active[0] = False
        print(confirmed[0])
        print(str(timer() - start), "sec runtime")
        for t in threading.enumerate():
            if t is not threading.currentThread():
                t.join()
        sys.exit(0)

for number in li:
    thread = threading.Thread(target=squareSum, args=(number,)).start()
    check(confirmed)


while len(threading.enumerate()) > 1:
    check(confirmed)
    time.sleep(1)

print("No solution was found")
