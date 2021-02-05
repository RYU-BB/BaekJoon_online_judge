from itertools import combinations

bit_list = [0 for _ in range(2000001)]

n = int(input())
s = list(map(int, input().split()))

for num in s:
    bit_list[num] = 1

for i in range(2, n + 1):
    combi = list(combinations(s, i))
    for j in range(len(combi)):
        bit_list[sum(combi[j])] = 1

for i in range(1, len(bit_list)):
    if bit_list[i] == 0:
        print(i)
        break
