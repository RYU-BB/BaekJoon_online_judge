n = int(input())
d = [1] * n
v = [0] * n
a = [int(x) for x in input().split()]
result = ""

for i in range(n):
    for j in range(i):
        if a[j] < a[i] and d[i] < d[j] + 1:
            d[i] = d[j] + 1
            v[i] = j + 1

print(max(d))

idx = d.index(max(d))
for _ in range(max(d)):
    result = str(a[idx]) + " " + result
    idx = v[idx] - 1

print(result)
