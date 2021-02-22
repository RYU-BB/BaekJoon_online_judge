n = int(input())
time_list = list(map(int, input().split()))

time_list.sort()
result = 0
pre_time = 0

for time in time_list:
    pre_time += time
    result += pre_time

print(result)