import sys

num = int(input())

if num == 1:
    sys.exit()

while num:
    for i in range(2, num + 1):
        if not num % i:
            print(i)
            break

    num = num // i