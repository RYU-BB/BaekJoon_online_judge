import math


n = int(input())
m = int(input())
ms = []
if m != 0:
    ms = list(input().split())

ans = math.inf
length = 0

for i in range(1000000):
    broken = False
    for s in str(i):
        if s in ms:
            broken = True
    if broken:
        pass
    else:
        if ans > abs(n - i):
            ans = abs(n - i)
            length = len(str(i))

ans = min(ans + length, abs(n - 100))

print(ans)