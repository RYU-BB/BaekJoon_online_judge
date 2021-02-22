n, k = map(int, input().split())
money = list()
count = 0

for _ in range(n):
    money.append(int(input()))

for i in range(n - 1, -1, -1):
    if k == 0:
        break
    if k < money[i]:
        continue
    count += k // money[i]
    k %= money[i]

print(count)