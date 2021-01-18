n = int(input())
cnt = 2
number = 1666
flag = False

if n == 1:
    number = 666

while True:
    if cnt == n:
        break
    num = list(map(int, str(number)))
    if num[0] == 6 and num[1] == 6 and num[2] == 6:
        if flag == False:
            for i in range(3, len(num)):
                num[i] = 0
            flag = True
        number += 1
    else:
        number += 1000
        flag = False
    cnt += 1

print(number)
