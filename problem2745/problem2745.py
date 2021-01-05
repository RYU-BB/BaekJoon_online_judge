input_num, base_n = map(str, input().split())
result = 0

for i in range(1,len(input_num)+1):
    num = ord(input_num[-i])
    if num < 58:
        num -= 48
    else:
        num -= 55

    result += num * (int(base_n) ** (i - 1))

print(result)