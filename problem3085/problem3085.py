def check(candy_list):
    n = len(candy_list)
    ans = 1

    for i in range(n):
        cnt = 1
        for j in range(n):
            if candy_list[i][j] == candy_list[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt:
                ans = cnt

        cnt = 1
        for j in range(n):
            if candy_list[j][i] == candy_list[j - 1][i]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt:
                ans = cnt

    return ans


n = int(input())
candy = list()

for i in range(n):
    candy.append(list(input()))

result = 0

for i in range(n):
    for j in range(n):
        if j + 1 < n:
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
            temp = check(candy)
            if result < temp:
                result = temp
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]

        if i + 1 < n:
            candy[i][j], candy[i + 1][j] = candy[i + 1][j], candy[i][j]
            temp = check(candy)
            if result < temp:
                result = temp
            candy[i][j], candy[i + 1][j] = candy[i + 1][j], candy[i][j]

print(result)
