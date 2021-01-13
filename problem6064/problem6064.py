import sys


input = sys.stdin.readline
test_num = int(input())

for _ in range(test_num):
    m, n, x, y = map(int, input().split())
    count = 1
    x -= 1
    y -= 1
    flag = False

    for k in range(x, n * m, m):
        if k % n == y:
            print(k + 1)
            flag = True
            break
    if not flag:
        print(-1)
