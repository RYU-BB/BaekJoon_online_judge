day_num = int(input())
cost = [[0, 0]] + [list(map(int, input().split())) for _ in range(day_num)]
max_cost = [0 for _ in range(day_num + 2)]
result = 0

for i in range(1, day_num + 2):
    for j in range(1, i):
        max_cost[i] = max(max_cost[i], max_cost[j])

        if j + cost[j][0] == i:
            max_cost[i] = max(max_cost[i], max_cost[j] + cost[j][1])
    result = max(result, max_cost[i])

print(result)
