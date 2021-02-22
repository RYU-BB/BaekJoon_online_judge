test_num = int(input())

for _ in range(test_num):
    n = int(input())
    coin = list(map(int, input().split()))
    money = int(input())

    dp = [0 for i in range(money + 1)]
    dp[0] = 1
    for i in coin:
        for j in range(1, money + 1):
            if j - i >= 0:
                dp[j] += dp[j - i]
    print(dp[money])