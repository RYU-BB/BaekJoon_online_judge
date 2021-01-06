n = int(input())
num_case = [1] * (n + 1)
num_case[1] = 1
result = 1
vip = 0
pre_vip = 0

for i in range(2, n + 1):
    num_case[i] = num_case[i - 1] + num_case[i - 2]

m = int(input())

for _ in range(m):
    vip = int(input())
    result *= num_case[vip - pre_vip - 1]
    pre_vip = vip

result *= num_case[n - vip]

print(result)