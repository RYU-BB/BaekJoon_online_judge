from itertools import combinations


n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
house = []
chicken = []
min_chicken_dis = float('inf')

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        if city[i][j] == 2:
            chicken.append([i, j])

for chicken_points in combinations(chicken, m):
    chicken_dis = 0
    for home_point in house:
        chicken_dis += min([abs(home_point[0] - chicken_point[0]) +
                            abs(home_point[1] - chicken_point[1]) for chicken_point in chicken_points])
    min_chicken_dis = min(min_chicken_dis, chicken_dis)

print(min_chicken_dis)