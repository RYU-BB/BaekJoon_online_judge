n = int(input())
pack = [0] + list(map(int, input().split()))
max_cost = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, i + 1):
        max_cost[i] = max(max_cost[i], max_cost[i - j] + pack[j])
        print("max_cost[", i, "] : ", max_cost[i])

print(max_cost[n])
