n = int(input())
d = [0] * n
a = [int(x) for x in input().split()]

for i in range(n):
    d[i] = max(d[i - 1] + a[i], a[i])

print(max(d))
