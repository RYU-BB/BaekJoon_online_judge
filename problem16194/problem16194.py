n = int(input())
pack = [0] + list(map(int, input().split()))
min_cost = pack[:]

for i in range(1, n+1):
    for j in range(1, i+1):
        min_cost[i] = min(min_cost[i], min_cost[i - j] + pack[j])

print(min_cost[n])