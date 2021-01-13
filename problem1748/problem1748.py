num = int(input())
count = 0
start = 1
len = 1
flag = False
ans = 0

while True:
    end = start * 10 - 1
    if end > num:
        end = num
        flag = True

    ans += (end - start + 1) * len
    start *= 10
    len += 1

    if flag:
        break

print(ans)