def check(num):
    num = list(str(num))
    for n in num:
        if n in broken_num:
            return False
    return True


max = 1000001

channel_num = int(input())
m = int(input())
broken_num = list(input().strip())
result = abs(channel_num - 100)

for i in range(max):
    if check(i):
        result = min(result, len(str(i)) + abs(i - channel_num))
print(result)
