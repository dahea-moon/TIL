import sys
import time
sys.stdin = open("input.txt", "r")

T = 10
stime = time.time()
for tc in range(1, T+1):
    N = int(input())
    H = list(map(int,input().split()))
    count = 0
    for i in range(2, N-2):
        check = [H[i-2], H[i-1], H[i], H[i+1], H[i+2]]
        check = sorted(check)
        if H[i] == check[-1]:
            count += check[-1] - check[-2]
    print("#{} {}".format(tc, count))
etime = time.time() - stime
print(etime)