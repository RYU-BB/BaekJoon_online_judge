n = int(input())
d = [1] * (n + 1)
a = [int(x) for x in input().split()]

for i in range(n):
    for j in range(i):
        if a[j] < a[i] and d[i] < d[j] + 1:
            d[i] = d[j] + 1

print(max(d))