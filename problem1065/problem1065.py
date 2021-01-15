n = int(input())
cnt = 99

if n < 100:
    cnt = n
else:
    for i in range(100, n + 1):
        num = list(map(int, list(str(i))))
        if num[0] - num[1] == num[1] - num[2]:
            cnt += 1

print(cnt)