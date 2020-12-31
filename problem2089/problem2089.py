num = int(input())
result = ''

if not num:
    print(0)
    exit()

while num:
    result = str(abs(num % -2)) + result
    if num % -2:
        num = num // -2 + 1
    else:
        num = num // -2

print(result)