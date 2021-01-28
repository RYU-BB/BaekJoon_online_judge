import sys


n = int(input())
num_list = list(map(int, input().split()))
i = n - 1

while i > 0 and num_list[i - 1] >= num_list[i]:
    i -= 1

if i <= 0:
    print(-1)
    sys.exit()

j = n - 1
while num_list[i - 1] >= num_list[j]:
    j -= 1

num_list[i - 1], num_list[j] = num_list[j], num_list[i - 1]

j = n - 1
while i < j:
    num_list[i], num_list[j] = num_list[j], num_list[i]
    i += 1
    j -= 1

print(*num_list)