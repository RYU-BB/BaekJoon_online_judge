def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


n, s = map(int, input().split())
a = list(map(int, input().split()))
distance = list()

for location in a:
    distance.append(abs(location-s))

result = distance[0]
for i in range(1, n):
    result = uc(result, distance[i])

print(result)