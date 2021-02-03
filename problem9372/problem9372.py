import sys
input = sys.stdin.readline


test_n = int(input())

for _ in range(test_n):
    n, m = map(int, input().split())
    for _ in range(m):
        input()
    print(n - 1)
